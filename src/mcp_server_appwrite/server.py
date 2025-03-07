import asyncio
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.shared.exceptions import McpError
import mcp.server.stdio
import argparse
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.services.users import Users
from appwrite.services.teams import Teams
from appwrite.services.storage import Storage
from appwrite.services.functions import Functions
from appwrite.services.locale import Locale
from appwrite.services.avatars import Avatars
from appwrite.services.messaging import Messaging
from appwrite.exception import AppwriteException
from .tool_manager import ToolManager
from .service import Service

parser = argparse.ArgumentParser(description='Appwrite MCP Server')
parser.add_argument('--projectId', required=True, help='Your Appwrite project ID')
parser.add_argument('--apiKey', required=True, help='Your Appwrite API key')
parser.add_argument('--endpoint', required=False, help='Your Appwrite endpoint', default='https://cloud.appwrite.io/v1')
args = parser.parse_args()

# Initialize Appwrite client
client = Client()
client.set_endpoint(args.endpoint)
client.set_project(args.projectId)
client.set_key(args.apiKey)

# Initialize tools manager and register services
tools_manager = ToolManager()
tools_manager.register_service(Service(Users(client), "users"))
tools_manager.register_service(Service(Teams(client), "teams"))
tools_manager.register_service(Service(Databases(client), "databases"))
tools_manager.register_service(Service(Storage(client), "storage"))
tools_manager.register_service(Service(Functions(client), "functions"))
tools_manager.register_service(Service(Messaging(client), "messaging"))
tools_manager.register_service(Service(Locale(client), "locale"))
tools_manager.register_service(Service(Avatars(client), "avatars"))

async def serve() -> Server:
    server = Server("Appwrite MCP Server")
    
    @server.list_tools()
    async def handle_list_tools() -> list[types.Tool]:
        return tools_manager.get_all_tools()

    @server.call_tool()
    async def handle_call_tool(
        name: str, arguments: dict | None
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        
        try:
            tool_info = tools_manager.get_tool(name)
            if not tool_info:
                raise McpError(f"Tool {name} not found")
            
            bound_method = tool_info["function"]
            result = bound_method(**(arguments or {}))
            if hasattr(result, 'to_dict'):
                result_dict = result.to_dict()
                return [types.TextContent(type="text", text=str(result_dict))]
            return [types.TextContent(type="text", text=str(result))]
        except AppwriteException as e:
            return [types.TextContent(type="text", text=f"Appwrite Error: {str(e)}")]
        except Exception as e:
            return [types.TextContent(type="text", text=f"Error: {str(e)}")]

    return server

async def _run():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        server = await serve()
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="appwrite",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(_run())