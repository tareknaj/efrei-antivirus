# Configuration Ubuntu
```
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-venv python3-pip -y
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Installer l'extension Python debugger dans WSL et les autres

# Tester l'application
2 options :
- Si plusieurs fonctions : `python app.py scan --path "C:\Users\tarek\workspace\efrei-python\test"`
- Pour exécuter la fonctionnalité principale par défaut : `python app.py "C:\Users\tarek\workspace\efrei-python\test"`

Linux:
- Si plusieurs fonctions : `python app.py scan "/home/tarek/efrei-python/test"`
- Pour exécuter la fonctionnalité principale par défaut : `python app.py "/home/tarek/efrei-python/test"`

# Deboguer
Ouvrir le fichier "app.py"
Run and debug
Dans parametre mettre : "/home/tarek/efrei-python/test"

# Passwords
tarek: tarek
test: test