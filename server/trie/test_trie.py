import pytest
import trie.trie as trie

def test_add_word():
    """
    Tests adding a word to the trie with the search method
    """
    test_trie = trie.Trie()
    test_trie.add_word("hello")
    assert test_trie.search("hello") == True

def test_add_word_spaced():
    """
    Tests adding words with spaces in the trie with the search method
    """
    test_trie = trie.Trie()
    test_trie.add_word("hello world")
    assert test_trie.search("hello world") == True

def test_search_word_not_in_trie():
    """
    Tests searching a word not in the trie with the search method
    """
    test_trie = trie.Trie()
    assert test_trie.search("") == False

def test_search_word_in_trie():
    """
    Tests searching a word in the trie
    """
    test_trie = trie.Trie()
    test_trie.add_word("slingshot")
    assert test_trie.search("slingshot") == True

def test_deleting_word_not_in_trie():
    """
    
    """