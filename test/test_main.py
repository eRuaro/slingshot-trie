import sys
from typer.testing import CliRunner

sys.path.append('..')
from ..main import app

runner = CliRunner()