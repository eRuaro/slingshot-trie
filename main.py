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
def suggestions(prefix : str = typer.Argument(...), suggestion_nums : int = typer.Argument(5)):
    """
    Returns a list of suggestions for a given prefix in the Trie API. Defaults to giving the top 5    
    """       
    response_url = url + "/suggestions/" + prefix + "?suggestion_nums=" + str(suggestion_nums)       
    response = requests.get(response_url)      
    for i in range(len(response.json())):
        typer.echo(response.json()[i])
        
@app.command()
def display(display_nums : int = typer.Argument(5), display_all : bool = typer.Argument(False)):
    """
    Displays the words in the Trie API server. Defaults to displaying the top 5 words.
    """
    response_url = url + "/display-trie"            
    response = requests.get(response_url)   
    typer.echo(response.json())
    if display_all:
        for i in range(len(response.json())):        
            typer.echo(response.json()[i])
    else:
        if display_nums > len(response.json()):
            for i in range(len(response.json())):
                typer.echo(response.json()[i])
        else:
            for i in range(display_nums):
                typer.echo(response.json()[i])

if __name__ == "__main__":
    app()