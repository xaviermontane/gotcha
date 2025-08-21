import typer
from core import social_scan
from pyfiglet import Figlet

from typing_extensions import Annotated

def main():
    """Display ASCII banner"""
    f = Figlet(font="slant")
    print(f.renderText("Gotcha!"))
    print("-- v0.1 (Alpha)\n")

# Create a Typer app instance
app = typer.Typer()

@app.command()
def scan(
    username: Annotated[str, typer.Argument()], 
    platforms: Annotated[str, typer.Option("--platforms", "-p", help="Comma-separated list of platforms to scan (e.g., Twitter,Reddit)")] = "Twitter,Reddit"
):
    """Scan a username across specified platforms."""
    typer.echo(f"Scanning @{username} on {platforms}")
    results = social_scan(username, platforms)
    typer.echo(f"Scan complete for @{username} on {platforms}")
    typer.echo("\nResults:")
    for platform, details in results["platforms"].items():
        typer.echo(f" - {platform}: {'Exists' if details['exists'] else 'Does not exist'}")

if __name__ == "__main__":
    main()
    app()