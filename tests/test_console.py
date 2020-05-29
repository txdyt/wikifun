import click.testing
import pytest

from wikifun import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_request_get(mocker):
    return mocker.patch("requests.get")


def test_main_succeeds(runner, mock_request_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
