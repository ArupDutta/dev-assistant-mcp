from datetime import date
from pathlib import Path
import json


WORKLOG_FILE = "worklogs.json"


def add_note(note: str) -> str:
    """ Adds a note to today's worklog.
    Creates the file/date entry if it doesn't exist.
    """

    today = date.today().strftime("%d-%m-%Y")  # e.g. 22-06-2026

    if Path(WORKLOG_FILE).exists():
        with open(WORKLOG_FILE, "r", encoding="utf-8") as f:
            worklogs = json.load(f)
    else:
        worklogs = {}


    if today not in worklogs:
        worklogs[today] = []


    worklogs[today].append(note)


    with open(WORKLOG_FILE, "w", encoding="utf-8") as f:
        json.dump(worklogs, f, indent=4)
    
    return f"note added!"


    

def get_note(target_date: str = None) -> str:
    """
    Retrieve worklog entries for a given date.

        Args:
        target_date (str, optional): Date in DD-MM-YYYY format.
        If not provided, the current date is used.

        Returns:
        str: Formatted worklog containing all notes for the specified
            date. Returns an empty worklog section if no notes exist.

        Example:
        get_note("22-06-2026")
        22-06-2026's Worklog:
        - Implemented MCP server
        - Reviewed pull requests
        
    """


    today = date.today().strftime("%d-%m-%Y")  # e.g. 22-06-2026


    with open(WORKLOG_FILE, "r", encoding="utf-8") as f:
            worklogs = json.load(f)


    if target_date == "None":
         target_date = today
    

    if target_date in worklogs:
         note = worklogs[target_date]
    else:
         note = []

    output = f"{target_date}'s Worklog: \n" + "\n".join(f"- {n}" for n in note)

    return (output)


#result = add_note("Completed training on uipath ai agent")
#result = get_note("None")
#print (result)