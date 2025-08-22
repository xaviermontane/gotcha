import os
import json
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
    platforms: Annotated[str, typer.Option("--platforms", "-p", help="Comma-separated list of platforms to scan (e.g., Twitter,Reddit)")] = "Instagram, Facebook, Twitter, Reddit, YouTube",
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Show all platforms (existing and non-existing)")] = False,
    output: Annotated[str | None, typer.Option("--output", "-o", help="Output file to save results (not implemented yet)")] = None
):
    """Scan a username across specified platforms."""
    # Display banner at start of scan
    display_banner()
    
    typer.echo(f"Scanning @{username} on {platforms}")
    results = social_scan(username, platforms)
    typer.echo(f"Scan complete for @{username} on {platforms}")
    typer.echo("\nResults:")
    
    # Filter results based on verbose flag
    for platform, details in results["platforms"].items():
        # Only show if verbose=True OR if the platform exists
        if verbose or details['exists'] == True:
            typer.echo(f" - {platform}: {'Exists' if details['exists'] else 'Does not exist'}")
    
    # Show summary if not verbose
    if not verbose:
        total_platforms = len(results["platforms"])
        existing_count = sum(1 for details in results["platforms"].values() if details['exists'])
        non_existing_count = total_platforms - existing_count
        
        if non_existing_count > 0:
            typer.echo(f"\n{non_existing_count} platforms not found. Use --verbose to see all results.")

    # Output results to file if specified
    folder = "output"
    os.makedirs(folder, exist_ok=True)
    
    if output:
        with open(os.path.join(folder, output), "w") as f:
            json.dump(results, f, indent=4)

        typer.echo(f"Results saved to '{os.path.join(folder, output)}' successfully!")

if __name__ == "__main__":
    app()