"""
Module princinpal
"""
import typer
from scanner import scan_directory

#Crée un objet app de type Typer
app = typer.Typer(help="Mini antivirus en ligne de commande (Typer).")

@app.command()
def scan(path: str):
    """
    Scanne un dossier pour détecter les fichiers suspects ou infectés.
    """
    typer.echo(f"[INFO] Lancement du scan sur : {path}")
    scan_directory(path)

@app.command()
def apropos():
    """
    A Propos
    """
    typer.echo("[INFO] Creation Tarek NAJEM")

#Chaque fichier Python est un module.
#Python donne à chaque module une variable spéciale __name__.
#Cette variable dit comment le fichier est utilisé.
if __name__ == "__main__":
    app()
