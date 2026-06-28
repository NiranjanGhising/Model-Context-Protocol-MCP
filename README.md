# Model Context Protocol Demo

This repository is a small Model Context Protocol (MCP) demo built around two Python entry points:

- `mcp_server.py` starts a FastMCP server that exposes document tools, resources, and a prompt.
- `mcp_client.py` connects to that server over stdio and lists the available tools.

The server currently keeps its documents in memory, so any edits are lost when the process exits.

## What It Demonstrates

This project is useful as a minimal reference for how to:

- expose tools with MCP
- expose resources with MCP
- expose prompts with MCP
- connect to a local MCP server from a Python client

## Project Structure

- `mcp_server.py` - MCP server implementation
- `mcp_client.py` - example client that connects to the server
- `README.md` - project overview and usage instructions
- `.gitignore` - ignores local secrets, caches, and virtual environments

## Requirements

- Python 3.12 or newer
- `mcp`
- `pydantic`

If you want an isolated environment, create a virtual environment first.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install mcp pydantic
```

If you prefer `uv`, you can use it to manage the environment and install the same dependencies.

## Run The Server

```bash
python mcp_server.py
```

This starts the MCP server defined in `mcp_server.py`.

## Run The Client

In a second terminal, after the server is available:

```bash
python mcp_client.py
```

The client connects to the server, calls `list_tools()`, and prints the tool names and descriptions.

## Available MCP Features

### Tools

- `read_document(doc_id)` - returns the text for a document ID
- `edit_document(doc_id, old_str, new_str)` - replaces text in a document

### Resources

- `doc://documents` - lists all available document IDs
- `doc://documents/{doc_id}` - returns the content for a specific document

### Prompt

- `format(doc_id)` - creates a prompt that asks the model to rewrite a document in Markdown

## Example Documents

The server starts with a small in-memory document store containing:

- `deposition.md`
- `report.pdf`
- `outlook.pdf`
- `plan.md`
- `spec.txt`

You can extend the demo by adding more entries to the `docs` dictionary in `mcp_server.py`.

## Notes

- The document store is in memory only.
- `edit_document()` updates the running process, not files on disk.
- `.env`, `__pycache__`, and `.venv` are ignored so local development artifacts stay out of Git.

## Next Steps

Good follow-up improvements for this repo would be:

- add persistence for documents
- return the updated document from `edit_document()`
- add more prompts for formatting or summarization workflows
- add tests for the server tools and client connection flow
