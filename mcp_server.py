from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

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
    doc_id: str= Field(description="ID of the document to edit"),
    old_str: str= Field(description="The exact text to replace (including whitespace)"),
    new_str: str= Field(description="The new text to insert in place of the old text")
):
    if doc_id not in docs:
        raise ValueError(f"doc file with {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str,new_str)



@mcp.resource(
    "doc://documents",
    mime_type="application/json"
)
def list_doc() -> list[str]:
    return list(docs.keys())


#TODO: Write a resource which returns the content of a particular docs

@mcp.resource(
    "doc://documents/{doc_id}",
    mime_type="text/plain"
)
def extract_doc(doc_id:str) -> str:

    if doc_id not in docs:
        raise ValueError(f"Doc with {doc_id} not found")
    
    return docs[doc_id]



@mcp.prompt(
    name="format",
    description="rewrite the contents of the documents in the markdown format."
)
def format_document(
    doc_id:str= Field(description="Id of the document to format."),


) -> list[base.Message]:
    prompt = """
                Your goal is to reformat a document to be written with markdown syntax.

                The id of the document you need to reformat is:
                <document_id>
                {doc_id}
                </document_id>

                Add in headers, bullet points, tables, etc as necessary. Feel free to add in structure.
                Use the 'edit_document' tool to edit the document. After the document has been reformatted...
            """
    return [base.UserMessage(prompt)]
    
 




if __name__ == "__main__":
    mcp.run()