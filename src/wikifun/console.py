import click

from . import __version__


@click.command()
@click.version_option(versoon=__version__)
def main():
    """The wikifun Python project."""
    click.echo("Hello, world!")
