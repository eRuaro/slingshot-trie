from typing import Optional
from fastapi import FastAPI
import trie.trie as trie

app = FastAPI()
trie = trie.Trie()


@app.get("/")
async def read_root():
    return {"Hello!": "This is a Trie API!"}

@app.put("/addWord/{word}")
async def add_word(word: str):
    trie.addWord(word)                   
    return {"status": "ok"}

@app.get("/suggestions/{prefix}")
async def get_suggestions(prefix : str, suggestion_nums=5):
    suggestions = trie.suggest(prefix)
    return {"suggestions": suggestions[:suggestion_nums]}