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

def test_delete_word_in_trie():
    """
    Tests deleting a word in the Trie API server
    """
    result = runner.invoke(app, ["delete-word", "test"])       
    assert result.exit_code == 0       
    assert "test deleted from Trie\n" in result.stdout

def test_delete_word_not_in_trie():
    """
    Tests deleting a word not in the Trie API server
    """
    result = runner.invoke(app, ["delete-word", "test"])
    assert result.exit_code == 0
    # test was previously deleted in an earlier test function
    assert "test does not exist in Trie\n" in result.stdout

def test_suggestions_default():
    """
    Tests suggestions given a prefix and with default n=5 parameter
    """
    runner.invoke(app, ["add-word", "hey"])
    runner.invoke(app, ["add-word", "heo"])
    runner.invoke(app, ["add-word", "heu"])
    runner.invoke(app, ["add-word", "hei"])
    runner.invoke(app, ["add-word", "hee"])
    runner.invoke(app, ["add-word", "hef"])
    result = runner.invoke(app, ["suggestions", "he"])
    assert result.exit_code == 0
    assert "hey\nheo\nheu\nhei\nhee\n" in result.stdout

def test_suggestions_modified():
    """
    Tests suggestions given a prefix and with default n=3 parameter
    """
    runner.invoke(app, ["add-word", "hey"])
    runner.invoke(app, ["add-word", "heo"])
    runner.invoke(app, ["add-word", "heu"])
    runner.invoke(app, ["add-word", "hei"])
    runner.invoke(app, ["add-word", "hee"])
    runner.invoke(app, ["add-word", "hef"])
    result = runner.invoke(app, ["suggestions", "he", "--n", "3"])
    assert result.exit_code == 0
    assert "hey\nheo\nheu\n" in result.stdout

def test_display_default():
    """
    Tests displaying the words in the Trie with the default n=5 parameter
    """
    result = runner.invoke(app, ["display"])
    assert result.exit_code == 0
    assert "hey\nheo\nheu\nhei\nhee\n" in result.stdout

def test_display_modified():
    """
    Tests displaying the words in the Trie with n=3 parameter
    """ 
    result = runner.invoke(app, ["display", "--n", "3"])
    assert result.exit_code == 0
    assert "hey\nheo\nheu\n" in result.stdout

def test_display_all():
    """
    Tests displaying all the words in the Trie
    """
    result = runner.invoke(app, ["display", "--all"])
    assert result.exit_code == 0
    assert "hey\nheo\nheu\nhei\nhee\nhef\ntest test\n" in result.stdout

def test_display_all_modified():
    """
    Tests displaying all the words in the Trie wherein n=3 is used
    """
    result = runner.invoke(app, ["display", "--n", "3", "--all"])
    assert result.exit_code == 0
    assert "hey\nheo\nheu\nhei\nhee\nhef\ntest test\n" in result.stdout