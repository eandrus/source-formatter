from typing import Optional

import typer

app = typer.Typer()

@app.command()
def format(
    location: Optional[str] = None,
    author: Optional[str] = None,
    date: Optional[str] = None,
    date_accessed: Optional[str] = None,
    title: Optional[str] = None,
    location_link: Optional[str] = None,
):
    """
    Format a citation for a source.
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

@app.command()
def hello(name: Optional[str] = None):
    if not name:
        name = typer.prompt("What is your name?")
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    app()