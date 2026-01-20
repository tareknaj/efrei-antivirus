import os
import shutil


def delete_file(path: str):
    print(f"[DELETE] {path}")
    os.remove(path)


def quarantine_file(path: str, quarantine_dir: str):
    filename = os.path.basename(path)
    quarantined = os.path.join(quarantine_dir, filename)

    shutil.move(path, quarantined)
    os.chmod(quarantined, 0o600)
    os.rename(quarantined, quarantined + ".quarantined")

    print(f"[QUARANTINE] {path} → {quarantined}")
