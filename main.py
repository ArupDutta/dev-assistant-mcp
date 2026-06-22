from fastmcp import FastMCP
import notes


WORKLOG_FILE = "worklogs.json"


mcp = FastMCP("Dev Assistant MCP Server")



@mcp.tool
def add_note(note: str) -> str:
    """ Adds a note to today's worklog.
    Creates the file/date entry if it doesn't exist.
    """

    return notes.add_note(note)



@mcp.tool
def get_note(target_date: str = "None") -> str:
    """
    Retrieve worklog entries for a given date.

        Args:
        date (str, optional): Date in YYYY-MM-DD format.
        If not provided, the current date is used.

        Returns:
        str: Formatted worklog containing all notes for the specified
            date. Returns an empty worklog section if no notes exist.

        Example:
        get_note("2026-06-22")
        2026-06-22's Worklog:
        - Implemented MCP server
        - Reviewed pull requests
        
    """

    return notes.get_note(target_date)




if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
