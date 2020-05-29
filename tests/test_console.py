import click.testing
import pytest

from wikifun import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_request_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock


def test_main_succeeds(runner, mock_request_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner, mock_request_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_requests_get(runner, mock_request_get):
    runner.invoke(console.main)
    assert mock_request_get.called


def test_main_uses_en_wikipedia_org(runner, mock_request_get):
    runner.invoke(console.main)
    args, _ = mock_request_get.call_args
    assert "en.wikipedia.org" in args[0]
