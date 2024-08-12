from typing import Optional

import typer

app = typer.Typer()

@app.command()
#Location name, Author, date, date accessed, title, location link
def format(
    location: Optional[str],
    author: Optional[str],
    date: Optional[str],
    date_accessed: Optional[str],
    title: Optional[str],
    location_link: Optional[str]
    ):
    """
    Format a citation for a location.
    """
    if not location:
        location = typer.prompt("Name of location (e.g. 'Wikipedia')")
    if not author:
        author = typer.prompt("Name of author")
    if not date:
        date = typer.prompt("Date of publication (e.g. '2021/01/01')")
    if not date_accessed:
        date_accessed = typer.prompt("Date accessed (e.g. '2021/01/01')")
    if not title:
        title = typer.prompt("Title of the publication")
    if not location_link:
        location_link = typer.prompt("Link to the location")
    
    citation = f"""
{location}; {author};
{date}; {date_accessed};
{title};
{location_link}
"""
    typer.echo(citation)