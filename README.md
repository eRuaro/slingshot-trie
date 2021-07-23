# Trie Data Structure
Implementation of a Trie data structure. The CLI-application was created using [Typer](https://typer.tiangolo.com/).

## Installation
1. Clone the repo:
   `git clone https://github.com/eRuaro/slingshot-trie`
2. Install modules:
    `pip install fastapi, typer, pytest`

## Folder Structure
```
├───server
│   ├───tests
│   │   ├───test_trie.py  
│   │   └───test_main.py
|   |
│   ├───trie
│   │   ├───trie.py
|   |
│   └───main.py
├───test
│   ├───test_main.py
|
└───main.py
```

The `main.py` file contains the cli-application itself while the `test/test_main.py` contains the test suite for the cli-application.

The `server` directory contains the underlying code of the Trie data structure, and the API I created out of it. `server/main.py` contains the API code, while `server/trie/trie.py` contains the Trie data structure. `server/tests` directory contains the test suites of the API and the Trie data structure.

## Using the CLI
#### 1. Adding a word
   `python main.py add-word word`
   
   Adding a phrase / sentence / words seperated by spaces:

   `python main.py add-word "word or phrase"`
#### 2. Deleting a word
   `python main.py delete-word "word"`
   
   Deleting a phrase / sentence / words seperated by spaces:
   
   `python main.py delete-word "word or phrase"`
#### 3. Searching a word
   `python main.py search-word word`
   
   Searching a phrase:

   `python main.py search-word "word or phrase"`
#### 4. Getting suggestions 
   `python main.py suggestions your_prefix`
   
   Getting *n* suggestions:

   `python main.py suggestions your_prefix --n your_n`
#### 5. Displaying words in the trie
   `python main.py display`
    - This will display the top 5 words in the Trie
   
   Displaying *n* words in the trie:

   `python main.py display --n your_n`
   
   Displaying all words in the trie:

   `python main.py display --all`
## Running tests
1. Navigate to either the `test` directory or the `server/tests` directory and run the command `pytest` to run the test cases.
