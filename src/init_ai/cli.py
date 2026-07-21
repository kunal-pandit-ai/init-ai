import typer

from init_ai import create # add_typer

from .commands.hello import hello
from .commands.author import author
from .commands.version import version
from .commands.who import who

app = typer.Typer()

app.command(help= "Welcome to You") (hello)
app.command(help= "Who created") (author)
app.command(help= "which version") (version)
app.command(help= "I am") (who)

app.add_typer(create.app, name="", help="Show message for Craete new projects")