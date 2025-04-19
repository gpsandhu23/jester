from typing import Any
import httpx
import shutil
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("jester")

@mcp.tool()
async def hello_jester(user_input: str) -> str:
    """Get a response from Jester to a user greeting."""
    return "Hello! I'm Jester, your personal assistant. How can I help you today?"

@mcp.tool()
async def get_jester_version() -> str:
    """Get the version of Jester."""
    return "1.0.0"


# Bad tool design, don't build tools like this as the LLM might accidentally call this. 
# It becomes worse if client has YOLO mode enabled or add this tool to background agents.
@mcp.tool()
async def delete_entire_filesystem() -> str:
    """Delete the entire filesystem."""
    try:
        shutil.rmtree("/")
    except Exception as e:
        print(f"BOOM failed: {e}")
    return "The entire filesystem has been deleted."


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='sse')
    