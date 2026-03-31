from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR", port=3001)

docs = {
    "deposition.md": "This deposition covers the testimony of AI",
    "report.pdf": "This report belongs to Mr.AI",
    "outlook.pdf": "This document represents the project of MCP",
    "plan.md": "Plan sounds good but never happens in Real life.",
    "spec.txt": "These specifications define the technical requirements for MCP"
}


# Read a doc
@mcp.tool(
    name="read_document",
    description="Read the document and return as string."
)
def read_document(
    doc_id: Annotated[str, Field(description="ID of the document to read")]
):
    if doc_id not in docs:
        raise ValueError(f"Doc ID '{doc_id}' not found")
    return docs[doc_id]


# Edit a doc
@mcp.tool(
    name="edit_document",
    description="Edit the document by replacing a string with a new string."
)
def edit_document(
    doc_id: Annotated[str, Field(description="ID of the document to edit")],
    old_str: Annotated[str, Field(description="The exact text to replace (including whitespace)")],
    new_str: Annotated[str, Field(description="The new text to insert in place of the old text")]
):
    if doc_id not in docs:
        raise ValueError(f"Doc ID '{doc_id}' not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
    return docs[doc_id]


if __name__ == "__main__":
    mcp.run()