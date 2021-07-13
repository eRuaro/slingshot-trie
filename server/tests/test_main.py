from fastapi.testclient import TestClient
import sys
  
# setting path - needed to get main
sys.path.append('..')

from ..main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() ==  {"Hello!": "This is a Trie API!"}

def test_post_method_add_word():
    """
    Tests adding a single word
    """
    response = client.post("/add-word/slingshot")
    assert response.status_code == 200
    assert response.json() == {"status": "slingshot added to Trie"}

def test_post_method_add_word2():
    """
    Tests adding two words
    """
    response = client.post("/add-word/slingshot is cool")
    assert response.status_code == 200
    assert response.json() == {"status": "slingshot is cool added to Trie"}

def test_delete_method_deleting_word_in_trie():
    """
    Tests deleting a word in the trie
    """
    #slingshot is already added in the trie per the test_post_method_add_word() function
    response = client.delete("/delete-word/slingshot")
    assert response.status_code == 200
    assert response.json() == {"status": "slingshot deleted from Trie"}

def test_delete_method_deleting_word_not_in_trie():
    """
    Tests deleting a word not in the trie
    """
    response = client.delete("/delete-word/sling")
    assert response.status_code == 200
    assert response.json() == {"status": "sling does not exist in Trie"}