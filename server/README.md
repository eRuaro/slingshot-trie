## Hosting
The server is hosted on Deta, the documentation of the API itself can be found [here](https://w0j5na.deta.dev/docs).

## CLI Interactioon
The CLI interacts with the server via numerous http calls. The methods `display`, `suggestions`, and `search-word` in the CLI performs a `get` request to the server. The method `add-word` performs a `post` request while the `delete-word` method performs a `delete` request.

## Framework used
The server was created via [FastAPI](https://fastapi.tiangolo.com/). The base url of the server is: https://w0j5na.deta.dev

## REST Endpoints
There are a total of 5 endpoints namely:
1. `/add-word/{word}`
   - `curl -X POST https://w0j5na.deta.dev/add-word/{word}`
2. `/delete-word/{word}`
   - `curl -X DELETE https://w0j5na.deta.dev/delete-word/{word}`
3. `/suggestions/{prefix}`
   - `curl https://w0j5na.deta.dev/suggestions/{prefix}`
4. `/search/{word}`
   - `curl https://w0j5na.deta.dev/search/{word}`
5. `/display-trie`
   - `curl https://w0j5na.deta.dev/display-trie`