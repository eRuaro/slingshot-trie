import typer
import requests

app = typer.Typer()
url = "https://w0j5na.deta.dev"

@app.command()
def add_word(word : str):
    """
    Adds word to the trie API
    """
    response_url = url + "/add-word/" + word
    response = requests.post(response_url)
    # typer.echo(response.status_code)
    typer.echo(response.json()["status"])
    

@app.command()
def search_word(word : str):
    """
    Searches if a word is in the Trie API server
    """
    response_url = url + "/search/" + word
    response = requests.get(response_url)
    typer.echo(response.json()["status"])
    
@app.command()
def delete_word(word : str):
    """
    Deletes a word in the Trie API server
    """
    response_url = url + "/delete-word/" + word
    response = requests.delete(response_url)
    typer.echo(response.json()["status"])

@app.command()
def suggestions(prefix : str, suggestion_nums = 5):
    """
    Returns a list of suggestions for a given prefix in the Trie API. Defaults to giving the top 5    
    """       
    response_url = url + "/suggestions/" + prefix + "?suggestion_nums=" + str(suggestion_nums)       
    response = requests.get(response_url)      
    for i in range(len(response.json())):
        typer.echo(response.json()[i])
        
    

if __name__ == "__main__":
    app()