# créer une fonction is_adult(age) qui retourne True si l'âge est supérieur ou égal à 18, sinon False.

**pour installer PyTest:** `pip install pytest`

## je créer age.py où j'écris ma fonction de calcul d'age.
Je rajouter aussi un contrôle de type avec `isinstance`:
`if not isinstance(age, int):
        raise ValueError("L'âge doit être un entier.")`

## Je créer test_age.py où je vais écrire mes tests.

Premier test: vérifier que 18 renvoie True en utilisant `assert`

`assert` vérifie qu'une expression est vraie.

dernier test: vérifier un type incorrecte, donc un string "dix-huit".
Pour gérer les cas d'erreurs, on utilise ValueError dans cette syntaxe:

`with pytest.raises(ValueError):
    is_adult("dix-huit")`




problème avec mon environnement qui détecte pas pytest:
faut aller dans view, tool windows, python packages et installer pytest.
