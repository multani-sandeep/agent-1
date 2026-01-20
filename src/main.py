import typer
from dotenv import load_dotenv
from .agent import run_agent

load_dotenv()

app = typer.Typer()

@app.command()
def generate(
    input: str = typer.Argument(..., help="Input text or file path"),
    file: bool = typer.Option(False, "--file", "-f", help="Treat input as a file path")
):
    """
    Generate a Mermaid diagram from text, PDF, or Image.
    """
    result = run_agent(input, is_file=file)
    print("\n--- Generated Mermaid Code ---\n")
    print(result)
    print("\n------------------------------\n")

if __name__ == "__main__":
    app()
