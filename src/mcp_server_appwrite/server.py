from mcp.server.fastmcp import FastMCP
import httpx
import argparse
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.exception import AppwriteException

# Initialize the MCP server
mcp = FastMCP("Appwrite MCP Server")

# Command-line argument parsing
parser = argparse.ArgumentParser(description='Appwrite MCP Server')
parser.add_argument('--projectId', required=True, help='Your Appwrite project ID')
parser.add_argument('--apiKey', required=True, help='Your Appwrite API key')
args = parser.parse_args()

# Initialize Appwrite client
client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')  # Default endpoint
client.set_project(args.projectId)
client.set_key(args.apiKey)

# Global instance of Databases service

databases_service = Databases(client)

@mcp.tool()
async def list_databases() -> str:
    """List all databases"""
    try:
        return databases_service.list()
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def list_collections(database_id: str) -> str:
    """List collections in a database"""
    try:
        return databases_service.list_collections(database_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def list_attributes(database_id: str, collection_id: str) -> str:
    """List attributes in a collection"""
    try:
        return databases_service.list_attributes(database_id, collection_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def list_documents(database_id: str, collection_id: str) -> str:
    """List documents in a collection"""
    try:
        return databases_service.list_documents(database_id, collection_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def list_indexes(database_id: str, collection_id: str) -> str:
    """List indexes in a collection"""
    try:
        return databases_service.list_indexes(database_id, collection_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_database(database_id: str, name: str, enabled: bool = True) -> str:
    """Create a new database"""
    try:
        return databases_service.create(database_id, name, enabled)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_database(database_id: str, name: str, enabled: bool = True) -> str:
    """Update an existing database"""
    try:
        return databases_service.update(database_id, name, enabled)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_collection(database_id: str, collection_id: str, name: str, permissions: list = None) -> str:
    """Create a new collection"""
    try:
        return databases_service.create_collection(database_id, collection_id, name, permissions)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_collection(database_id: str, collection_id: str, name: str, permissions: list = None) -> str:
    """Update an existing collection"""
    try:
        return databases_service.update_collection(database_id, collection_id, name, permissions)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_document(database_id: str, collection_id: str, document_id: str, data: dict, permissions: list = None) -> str:
    """Create a new document"""
    try:
        return databases_service.create_document(database_id, collection_id, document_id, data, permissions)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_document(database_id: str, collection_id: str, document_id: str, data: dict, permissions: list = None) -> str:
    """Update a document"""
    try:
        return databases_service.update_document(database_id, collection_id, document_id, data, permissions)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_index(database_id: str, collection_id: str, key: str, type: str, attributes: list, orders: list = None) -> str:
    """Create an index"""
    try:
        return databases_service.create_index(database_id, collection_id, key, type, attributes, orders)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_index(database_id: str, collection_id: str, key: str, type: str, attributes: list, orders: list = None) -> str:
    """Update an index"""
    try:
        return databases_service.update_index(database_id, collection_id, key, type, attributes, orders)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def get_document(database_id: str, collection_id: str, document_id: str) -> str:
    """Get a document"""
    try:
        return databases_service.get_document(database_id, collection_id, document_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def delete_document(database_id: str, collection_id: str, document_id: str) -> str:
    """Delete a document"""
    try:
        return databases_service.delete_document(database_id, collection_id, document_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def get_index(database_id: str, collection_id: str, key: str) -> str:
    """Get an index"""
    try:
        return databases_service.get_index(database_id, collection_id, key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def delete_index(database_id: str, collection_id: str, key: str) -> str:
    """Delete an index"""
    try:
        return databases_service.delete_index(database_id, collection_id, key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_string_attribute(database_id: str, collection_id: str, key: str, size: int, required: bool, default: str = None, array: bool = None) -> str:
    """Create a string attribute"""
    try:
        return databases_service.create_string_attribute(database_id, collection_id, key, size, required, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_string_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str, size: int = None, new_key: str = None) -> str:
    """Update a string attribute"""
    try:
        return databases_service.update_string_attribute(database_id, collection_id, key, required, default, size, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def delete_string_attribute(database_id: str, collection_id: str, key: str) -> str:
    """Delete a string attribute"""
    try:
        return databases_service.delete_attribute(database_id, collection_id, key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def get_database(database_id: str) -> str:
    """Get a database"""
    try:
        return databases_service.get(database_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def delete_database(database_id: str) -> str:
    """Delete a database"""
    try:
        return databases_service.delete(database_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def get_collection(database_id: str, collection_id: str) -> str:
    """Get a collection"""
    try:
        return databases_service.get_collection(database_id, collection_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def delete_collection(database_id: str, collection_id: str) -> str:
    """Delete a collection"""
    try:
        return databases_service.delete_collection(database_id, collection_id)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_boolean_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> str:
    """Create a boolean attribute"""
    try:
        return databases_service.create_boolean_attribute(database_id, collection_id, key, required, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_boolean_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> str:
    """Update a boolean attribute"""
    try:
        return databases_service.update_boolean_attribute(database_id, collection_id, key, required, default, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_datetime_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> str:
    """Create a datetime attribute"""
    try:
        return databases_service.create_datetime_attribute(database_id, collection_id, key, required, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_datetime_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> str:
    """Update a datetime attribute"""
    try:
        return databases_service.update_datetime_attribute(database_id, collection_id, key, required, default, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_email_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> str:
    """Create an email attribute"""
    try:
        return databases_service.create_email_attribute(database_id, collection_id, key, required, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_email_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> str:
    """Update an email attribute"""
    try:
        return databases_service.update_email_attribute(database_id, collection_id, key, required, default, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_enum_attribute(database_id: str, collection_id: str, key: str, elements: list, required: bool, default: str = None, array: bool = None) -> str:
    """Create an enum attribute"""
    try:
        return databases_service.create_enum_attribute(database_id, collection_id, key, elements, required, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_enum_attribute(database_id: str, collection_id: str, key: str, elements: list, required: bool, default: str, new_key: str = None) -> str:
    """Update an enum attribute"""
    try:
        return databases_service.update_enum_attribute(database_id, collection_id, key, elements, required, default, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_float_attribute(database_id: str, collection_id: str, key: str, required: bool, min: float = None, max: float = None, default: float = None, array: bool = None) -> str:
    """Create a float attribute"""
    try:
        return databases_service.create_float_attribute(database_id, collection_id, key, required, min, max, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_float_attribute(database_id: str, collection_id: str, key: str, required: bool, min: float, max: float, default: float, new_key: str = None) -> str:
    """Update a float attribute"""
    try:
        return databases_service.update_float_attribute(database_id, collection_id, key, required, min, max, default, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_integer_attribute(database_id: str, collection_id: str, key: str, required: bool, min: int = None, max: int = None, default: int = None, array: bool = None) -> str:
    """Create an integer attribute"""
    try:
        return databases_service.create_integer_attribute(database_id, collection_id, key, required, min, max, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_integer_attribute(database_id: str, collection_id: str, key: str, required: bool, min: int, max: int, default: int, new_key: str = None) -> str:
    """Update an integer attribute"""
    try:
        return databases_service.update_integer_attribute(database_id, collection_id, key, required, min, max, default, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_ip_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> str:
    """Create an IP address attribute"""
    try:
        return databases_service.create_ip_attribute(database_id, collection_id, key, required, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_ip_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> str:
    """Update an IP address attribute"""
    try:
        return databases_service.update_ip_attribute(database_id, collection_id, key, required, default, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_relationship_attribute(database_id: str, collection_id: str, related_collection_id: str, type: str, two_way: bool = None, key: str = None, two_way_key: str = None, on_delete: str = None) -> str:
    """Create a relationship attribute"""
    try:
        return databases_service.create_relationship_attribute(database_id, collection_id, related_collection_id, type, two_way, key, two_way_key, on_delete)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def create_url_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str = None, array: bool = None) -> str:
    """Create a URL attribute"""
    try:
        return databases_service.create_url_attribute(database_id, collection_id, key, required, default, array)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_url_attribute(database_id: str, collection_id: str, key: str, required: bool, default: str, new_key: str = None) -> str:
    """Update a URL attribute"""
    try:
        return databases_service.update_url_attribute(database_id, collection_id, key, required, default, new_key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def get_attribute(database_id: str, collection_id: str, key: str) -> str:
    """Get an attribute"""
    try:
        return databases_service.get_attribute(database_id, collection_id, key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def delete_attribute(database_id: str, collection_id: str, key: str) -> str:
    """Delete an attribute"""
    try:
        return databases_service.delete_attribute(database_id, collection_id, key)
    except AppwriteException as e:
        return str(e)

@mcp.tool()
async def update_relationship_attribute(database_id: str, collection_id: str, key: str, on_delete: str = None, new_key: str = None) -> str:
    """Update a relationship attribute"""
    try:
        return databases_service.update_relationship_attribute(database_id, collection_id, key, on_delete, new_key)
    except AppwriteException as e:
        return str(e)

if __name__ == "__main__":
    mcp.run(transport='stdio')