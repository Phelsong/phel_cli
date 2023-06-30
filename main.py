# libs
import typer
import rich
import sys
from pathlib import Path

# imports

# =========================
app = typer.Typer()
state = {"verbose": False}
# =========================


@app.callback()
def main():
    #arg parse
    pass
# ========================

@app.command("help")
def help():    
    print("help")

# ========================
@app.command("hello")
def hello():
    print(":wave:")


# ========================


# app.add_typer(other_app, name="other")


# @other_app.command("hello")
# def other_hello():
#    print("other")


# =======================

if __name__ == "__main__":
    args = sys.argv[1:]
    app(args)
