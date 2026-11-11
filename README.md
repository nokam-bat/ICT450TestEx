# Exercice 4.1 Calcul majorité

## Consignes

Implémentez une fonction `is_adult(age)` qui retourne `True` si l’âge est supérieur ou égal à 18, sinon `False`.

Écrivez ensuite plusieurs tests automatisés avec PyTest pour vérifier le bon fonctionnement de cette fonction.

Pour installer PyTest : `pip install pytest`

### Étapes:
* Implémenter la fonction à tester
* Écrire les tests
* Exécuter les tests.

# Explication du code de age.py

`isinstance` veut dire is instance of. "Est-ce que cet [élément] est du type [quelle catégorie?]"
=> Vérifie le type d'une variable
Elle prends deux arguments entre parenthèses:
isinstance(ce qu'on veut tester, le type attendu) et renvoie un résultat logique (True ou False).

`raise ValueError()` déclenche une erreur sur commande.

`if __name__ == "__main__":` c'est le point d'entrée du programme
=> __name__ c'est la variable qui contient le nom du fichier en cours d'exécution
=> `"__main__"` nom spécial de python
Donc si je tape dans ma console `python age.py` alors python attribue main à name, le test est vrai et la boucle s'exécute.

`.lower() `prends en compte majuscule et minuscule

`age = int(user_input` prends le text écrit par l'utilisateur `"20"` et le transforme en int `20`

# Explication du code de test_age.py
