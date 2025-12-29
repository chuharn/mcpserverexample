# deployment.py
from mcp.server.fastmcp import FastMCP


# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


def main() -> None:
    """Run the FastMCP server using the default transport."""
    # Default transport is stdio; change to "sse" or "streamable-http" as needed.
    mcp.run()


if __name__ == "__main__":
    main()