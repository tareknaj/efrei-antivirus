import os

LOGFILE = "scan.log"

def read_file(path: str) -> str:
    try:
        fd = os.open(path, os.O_RDONLY)
        content = os.read(fd, os.path.getsize(path))
        os.close(fd)
        return content.decode()
        #return content.decode("utf-8", errors="ignore")
    except (OSError, UnicodeDecodeError):
        return ""

def log(message: str):
    #Propriétaire peut lire & écrire
    #Groupe peut lire seulement
    #Autres peuvent lire seulement
    #Le préfixe 0o indique à Python que c’est un nombre en octal (base 8)
    fd = os.open(LOGFILE, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    os.write(fd, (message + "\n").encode())
    os.close(fd)

def read_file_old(path: str) -> str:
    try:
        with open(path, "r", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""