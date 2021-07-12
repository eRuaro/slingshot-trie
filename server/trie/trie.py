class Trie:
    def __init__(self):
        # Initializes trie data srtucture - uses a hashtable internally.
        self.trie = {}
        
    def addWord(self, word : str) -> None:
        """
        Adds a word to the trie.
        """
        if word not in self.trie.keys():
            # Sets the initial value to 1 as this is the first occurence of the word.
            self.trie[word] = 1
        else:
            # Increases the occurence of the word in the trie by 1. 
            self.trie[word] += 1

    def search(self, word : str) -> bool:
        """
        Searches for a word in the trie, returns a boolean value on the existence of the word in the trie.
        """
        if word not in self.trie.keys():
            return False
        else:
            return True

    def _by_value(self, item):
        """
        Private method for sorting the trie by the occurence of the words.
        """
        return item[1]

    def suggest(self, prefix : str) -> list:
        """
        Returns a list of suggestions for a given prefix.
        """
        suggestions = []
        
        # sorts the keys in the trie decreasing occurence of the words.
        for key in sorted(self.trie.items(), key=self._by_value, reverse=True):
            suggestions.append(key)

        return suggestions

    def getAllWords(self) -> list:
        """
        Returns a list of all the words in the trie, sorted in decreasing order.
        """
        return self.trie.keys()

    def delete(self, word : str) -> None:
        """
        Deletes a word from the trie
        """
        self.trie.pop(word, None)
