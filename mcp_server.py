from pydantic import Field
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level= "ERROR")

docs ={
    "deposition.md": "This deposition covers the testimony of AI",
    "report.pdf": "This report belongs to Mr.AI",
    "outlook.pdf": "This document represts the project of MCP",
    "plan.md": "Plan sounds good but never happens in Real life.",
    "spec.txt": "These specifications define the technical requirements for MCP"

}


#read a doc
@mcp.tool(
    name= "read a document",
    description= "Read the document and return as string."
)
def read_document(
    doc_id: str= Field(description = "ID of the documnet to read") 
):
    if doc_id not in docs:
        raise ValueError(f"Doc ID with {doc_id} not found")
    return docs[doc_id]



#edit a doc
@mcp.tool(
    name = "edit a document",
    description = "Read the documnet, Edit the document by replacing a string in the documents content with a new string. "
)

def edit_document(
    doc_id: str= Field(description = "ID of the document to read"),
    old_str: str= Field(description = "Including the whitespace, the text mmust match. the text to replace"),
    new_str: str= Field(description = "The next text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc ID with {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
    return docs[doc_id]

#TODO: Write a resource to return all doc id's
#TODO: Write a resource to return the contents of a particular doc
#TODO: Write a prompt to rewrite a doc in markdown format
#TODO: write a prompt to summaries of a doc
