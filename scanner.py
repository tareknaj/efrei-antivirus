import os
from actions import quarantine_file, delete_file
from utils import log, read_file

SIGNATURES = ("malware", "virus", "trojan", "ransom")
ALLOWED_EXT = (".txt", ".cfg", ".log")
MESSAGES = {
    "infected": "Fichier infecté !",
    "suspicious": "Fichier suspect !",
    "clean": "Fichier propre !"
}

def scan_file(path: str) -> str:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Fichier introuvable : {path}")

    content = read_file(path)

    # Détection simple
    for sig in SIGNATURES:
        if sig in content:
            return "infected"

    # Extension suspecte
    if not path.endswith(ALLOWED_EXT):
        return "suspicious"

    # Taille trop grande
    if os.path.getsize(path) > 500_000:
        return "suspicious"

    return "clean"

def scan_directory(directory: str):
    if not os.path.isdir(directory):
        raise NotADirectoryError("Le chemin fourni n'est pas un dossier.")

    list_files = os.listdir(directory)

    files = map(
        lambda f: os.path.join(directory, f),
        list_files
    )

    files = filter(os.path.isfile, files)

    quarantine_dir = os.path.join(directory, "quarantine")

    if not os.path.exists(quarantine_dir):
        os.mkdir(quarantine_dir)

    for file in files:
        try:
            status = scan_file(file)
            log(f"Fichier : {file} → {MESSAGES[status]}")

            if status == "infected":
                delete_file(file)

            elif status == "suspicious":
                quarantine_file(file, quarantine_dir)

        except FileNotFoundError as e:
            log(f"[ERROR] {e}")
        finally:
            pass

    log(f"Scan terminé. Process PID = {os.getpid()}")
    print("Scan terminé.")
