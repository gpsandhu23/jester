# Jester MCP Server

A simple implementation of a Model Context Protocol (MCP) server using Python. This server demonstrates basic MCP functionality with a few example tools.

## Overview

Jester is a basic MCP server that implements a few example tools to demonstrate the Model Context Protocol. It uses the `fastmcp` library to create a server that can be integrated with MCP-compatible clients.

## Features

- Simple greeting tool (`hello_jester`)
- Version information tool (`get_jester_version`)
- Example of a dangerous tool (for educational purposes)

## Prerequisites

- Python 3.10 or higher
- `uv` package manager

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd jester
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
uv pip install -e .
```

## Usage

Run the server:
```bash
uv run jester.py
```

The server will start and listen for MCP connections using Server-Sent Events (SSE) transport.

## Available Tools

### `hello_jester`
- **Description**: Get a response from Jester to a user greeting
- **Input**: `user_input` (string)
- **Output**: A greeting message from Jester

### `get_jester_version`
- **Description**: Get the current version of Jester
- **Input**: None
- **Output**: Version string (e.g., "1.0.0")

## Development

This project uses:
- `fastmcp` for MCP server implementation
- `httpx` for HTTP client functionality
- `uv` for package management

## Security Note

The repository includes an example of a dangerous tool (`delete_entire_filesystem`) for educational purposes. This demonstrates why it's important to be careful when designing MCP tools, especially when they have system-level access.
