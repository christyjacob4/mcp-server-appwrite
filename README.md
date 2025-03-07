# Appwrite MCP server

## Overview

A Model Context Protocol server for interacting with Appwrite's API. This server provides tools to manage databases, users, functions, teams, and more within your Appwrite project.

Currently the server supports the following tools:

- [x] Databases
- [x] Users
- [x] Teams
- [x] Messaging
- [x] Locale
- [x] Avatars
- [ ] Storage
- [ ] Functions
- [ ] Accounts

### Installation

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/), no specific installation is needed. We will use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *mcp-server-appwrite*.

### Using PIP

Alternatively, you can install `mcp-server-appwrite` via pip:

```
pip install mcp-server-appwrite
```

After installation, you can run it as a script using:

```
python -m mcp_server_appwrite
```

## Configuration

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
"mcpServers": {
  "appwrite": {
    "command": "uvx",
    "args": ["mcp-server-appwrite", "--projectId", "YOUR_PROJECT_ID", "--apiKey", "YOUR_API_KEY"]
  }
}
```

### Usage with [Zed](https://github.com/zed-industries/zed)

Add to your Zed settings.json:

```json
"context_servers": {
  "mcp-server-appwrite": {
    "command": "python",
    "args": ["-m", "mcp_server_appwrite", "--projectId", "YOUR_PROJECT_ID", "--apiKey", "YOUR_API_KEY"]
  }
}
```

## Development

```bash
uv pip install -e .
```

Run the server:

```bash
uv run -v mcp-server-appwrite --projectId YOUR_PROJECT_ID --apiKey YOUR_API_KEY --endpoint YOUR_ENDPOINT
```

## Debugging

You can use the MCP inspector to debug the server. For `uvx` installations:

```bash
npx @modelcontextprotocol/inspector uv run mcp-server-appwrite --projectId YOUR_PROJECT_ID --apiKey YOUR_API_KEY --endpoint YOUR_ENDPOINT
```

Or if you've installed the package in a specific directory or are developing on it:

```bash
npx @modelcontextprotocol/inspector \
  uv \
  --directory src/mcp_server_appwrite run mcp-server-appwrite \
  --projectId 67b9a5460035d2f0592b \
  --apiKey standard_19773360ab8f6350b6958ef596c7a849c515034f4cc7b09baa622788c34d40002e2f5ad7570bcbe06a81f845ba43b3e3086097ddc261a40d1396d6a048609a7a06ac88b8587e3a6ba5143626b819bb744a1266e9cdfa95fe2b537a41b2a8fafe6c73afd8d1ed4dcb8009f9b44407a0d72ed263ea34bf0c394324abfc8367029e
```

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.