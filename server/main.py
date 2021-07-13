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
    trie.addWord(word)                   
    return {"status": word +  " added to Trie"}

#prefix/?suggestions_nums=5
@app.get("/suggestions/{prefix}")
async def get_suggestions(prefix : str, suggestion_nums : Optional[int] = 5):
    suggestions = trie.suggest(prefix)
    return suggestions[:suggestion_nums]