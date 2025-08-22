import typer
from core import social_scan
from pyfiglet import Figlet
from typing_extensions import Annotated

# Create a Typer app instance
app = typer.Typer()

def display_banner():
    """Display ASCII banner"""
    f = Figlet(font="slant")
    print(f.renderText("Gotcha!"))
    print("-- v0.1 (Alpha)\n")

@app.command()
def scan(
    username: Annotated[str, typer.Argument()], 
    platforms: Annotated[str, typer.Option("--platforms", "-p", help="Comma-separated list of platforms to scan (e.g., Twitter,Reddit)")] = "Instagram, Facebook, Twitter, Reddit, YouTube"
):
    """Scan a username across specified platforms."""
    # Display banner at start of scan
    display_banner()
    
    typer.echo(f"Scanning @{username} on {platforms}")
    results = social_scan(username, platforms)
    typer.echo(f"Scan complete for @{username} on {platforms}")
    typer.echo("\nResults:")
    
    for platform, details in results["platforms"].items():
        typer.echo(f" - {platform}: {'Exists' if details['exists'] else 'Does not exist'}")

if __name__ == "__main__":
    app()