class Trie:
    def __init__(self):
        self.trie = {}
        
    def addWord(self, word : str) -> None:
        if word not in self.trie.keys():
            self.trie[word] = 1
        else:
            self.trie[word] += 1

    def search(self, word : str) -> bool:
        if word not in self.trie.keys():
            return False
        else:
            return True

    def _by_value(self, item):
        return item[1]

    def suggest(self, prefix : str, n_suggestions=5) -> list:
        if type(n_suggestions) != int:
            raise TypeError('n_suggestions must be an integer')

        suggestions = []
        
        for key in sorted(self.trie.items(), key=self._by_value, reverse=True):
            suggestions.append(key)

        return suggestions

    def delete(self, word : str) -> None:
        self.trie.pop(word, None)
