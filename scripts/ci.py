import click
import os


@click.command()
def check_release_gate():
    """Check if the release gate is open by searching
    for a file named release-gate.txt in the current
    working directory and seeing whether its contents
    read "open" or "closed".
    """
    if os.path.exists("release-gate.txt"):
        with open("release-gate.txt", "r") as f:
            status = f.read().strip()
        if status == "open":
            click.echo("Release gate is open... closing it")
            with open("release-gate.txt", "w") as f:
                f.write("closed")
        elif status == "closed":
            click.echo("Release gate is closed... opening it")
            with open("release-gate.txt", "w") as f:
                f.write("open")
        else:
            click.echo("Release gate status is unknown... setting to closed")
            with open("release-gate.txt", "w") as f:
                f.write("closed")
    else:
        # Create a release-gate.txt file with status "open"
        # if it doesn't exist
        with open("release-gate.txt", "w") as f:
            f.write("open")
        click.echo("Created release-gate.txt file with status 'open'")