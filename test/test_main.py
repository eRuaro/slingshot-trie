import sys
from typer.testing import CliRunner

# setting path - needed to get main
sys.path.append('..')

from main import app
runner = CliRunner()

def test_add_word():
    """
    Tests adding a word to the Trie API.
    """
    result = runner.invoke(app, ["add-word", "test"])
    assert result.exit_code == 0
    assert "test added to Trie\n" in result.stdout

def test_add_2words():
    """
    Tests adding two words seperated by spaces to the Trie API
    """
    result = runner.invoke(app, ["add-word", "test test"])
    assert result.exit_code == 0
    assert "test test added to Trie\n" in result.stdout

def test_search_word_in_trie():
    """
    Tests searching a word in the Trie API server 
    """
    result = runner.invoke(app, ["search-word", "test"])
    assert result.exit_code == 0
    # test was added to the trie in an earlier test function
    assert "test found in Trie!\n" in result.stdout

def test_search_word_not_in_trie():
    """
    Tests searching a word not in the Trie API server
    """
    result = runner.invoke(app, ["search-word", "slingshot"])
    assert result.exit_code == 0
    assert "slingshot not found in Trie!\n" in result.stdout

