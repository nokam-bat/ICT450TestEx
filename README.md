Cette fois, les tests sont déjà écrits : tu dois les exécuter, lire le rapport, puis corriger celui qui échoue. On commence par générer le rapport, sans modifier le code.

Crée le fichier test_recherche.py et coller le code fourni.

installer les outils : `python -m pip install pytest-html`

exécuter les tests de cet exercice et générer le rapport `python -m pytest test_recherche.py --html=rapport_tests.html --self-contained-html`

`--self-containe-html` : garde le rapport et sa mise en forme dans un seul fichier.

Ouvrir le rapport dans mon navigateur avec la commande `Start-Process .\rapport_tests.html`

## correction à la ligne 45 : écrire Bob au lieu de bob
