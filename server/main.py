from typing import Optional
from fastapi import FastAPI
import trie.trie as trie

app = FastAPI()
trie = trie.Trie()

@app.get("/")
async def read_root():
    return {"Hello!": "This is a Trie API!"}

@app.post("/add-word/{word}")
async def add_word(word: str):
    trie.add_word(word)                   
    return {"status": word +  " added to Trie"}

@app.delete("/delete-word/{word}")
async def delete_word(word: str):
    if trie.search(word):
        trie.delete(word)
        return {"status": word + " deleted from Trie"}
    else:
        return {"status": word + " does not exist in Trie"}

#prefix/?suggestions_nums=5
@app.get("/suggestions/{prefix}")
async def get_suggestions(prefix : str, suggestion_nums : Optional[int] = 5):
    suggestions = trie.suggest(prefix)
    return suggestions[:suggestion_nums]

@app.get("/search/{word}")
async def search_word(word : str):
    if trie.search(word):                   
        return {"status": word + " found in Trie!"}
    else:
        return {"status": word + " not found in Trie!"}

#display-trie?words_nums=5
@app.get("/display-trie")
async def display(words_nums : Optional[int] = 5):
    words = trie.get_all_words()
    return words[:words_nums]