import asyncio
import os
import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.shared.exceptions import McpError
from dotenv import load_dotenv
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

# Load environment variables from .env file
load_dotenv()

# Get environment variables
project_id = os.getenv('APPWRITE_PROJECT_ID')
api_key = os.getenv('APPWRITE_API_KEY')
endpoint = os.getenv('APPWRITE_ENDPOINT', 'https://cloud.appwrite.io/v1')

if not project_id or not api_key:
    raise ValueError("APPWRITE_PROJECT_ID and APPWRITE_API_KEY must be set in environment variables")

# Initialize Appwrite client
client = Client()
client.set_endpoint(endpoint)
client.set_project(project_id)
client.set_key(api_key)

# Initialize tools manager and register services
tools_manager = ToolManager()
tools_manager.register_service(Service(Users(client), "users"))
# tools_manager.register_service(Service(Teams(client), "teams"))
tools_manager.register_service(Service(Databases(client), "databases"))
# tools_manager.register_service(Service(Storage(client), "storage"))
# tools_manager.register_service(Service(Functions(client), "functions"))
# tools_manager.register_service(Service(Messaging(client), "messaging"))

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