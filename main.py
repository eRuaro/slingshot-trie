import typer
import requests

app = typer.Typer()
url = "https://w0j5na.deta.dev"

@app.command()
def add_word(word : str) -> None:
    """
    Adds word to the trie API
    """
    response_url = url + "/add-word/" + word
    response = requests.post(response_url)
    # typer.echo(response.status_code)
    # typer.echo(response.json()["status"])
    

@app.command()
def search_word(word : str) -> bool:
    """
    Searches if a word is in the Trie API server
    """
    

if __name__ == "__main__":
    app()