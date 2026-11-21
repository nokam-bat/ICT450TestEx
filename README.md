le prof a donné un fichier prix.py avec une fonction dedans pour calculer.

je peux utliser la commande `pytest test_prix.py` pour faire le test.


Je créer un fichier de test test_prix.py pour 5 tests unitaires respectant AAA.

**Pour le premier test standard:**
je dois importer la fonction de calcul.
j'établis les variables en leur donnant des données.
J'appelle la fonction importée à tester en stockant le résultat dans une variable comme ça 
`resultat = calculer_prix_ttc(prix_ht, tva)`
et je vérifie le résultat avec `assert` et `==`


**Pour le test de prix_ht négatif à -50**
je dois vérifier que l'appel déclenche une `ValueError` et on utilise PAS assert.

**Pour le test du pricx au 0:**
c'est autorisé juste faut assert que ça vient à 0.0


j'ai lancé `python -m pytest test_prix.py -v`