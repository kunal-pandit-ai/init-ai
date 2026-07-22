import typer

from .commands.hello import hello
from .commands.author import author
from .commands.version import version
from .commands.who import who
from .commands.pwd import pwd
from .commands.ls import ls
from .commands.mkdir import mkdir
from .commands.file import touch
from .commands.rm import rm
from .commands.cat import cat
from .commands.copy import copy
from .commands.write import write
from .commands.mv import mv
from .commands.tree import tree
from .commands.create import create
from .commands.doctor import doctor
from .commands.config import app as config_app

app = typer.Typer()

app.command(help= "Welcome to You") (hello)
app.command(help= "Who created") (author)
app.command(help= "which version") (version)
app.command(help= "I am") (who)
app.command(help= "Check current working directory") (pwd)
app.command(help= "Check files in dir") (ls)
app.command(help= "create Directory") (mkdir)
app.command(help= "craete a file") (touch)
app.command(help= "Delete file") (rm)
app.command(help="show content of file") (cat)
app.command(help="Duplicate file") (copy)
app.command(help="Write inside file") (write)
app.command(help="Rename file names") (mv)
app.command(help="Project map") (tree)
app.command(help="Setup Project") (create)
app.command(help="check Setup Project alright") (doctor)

app.add_typer(
    config_app,
    name="config"
)