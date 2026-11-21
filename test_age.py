# on importe la fonction crée pour vérifier que la personne est majeure
from age import is_adult

import pytest

# on appelle la fonction avec le chiffre 18 et on vérifie qu'elle renvoie True.
def test_age_18():  # on écrit 18 dans le nom de la fonction pour dire qu'on test 18 ans
    assert is_adult(18) is True


# vérifie mineur
def test_age_17():
    assert is_adult(17) is False

# vérifie + que 18
def test_age_19():
    assert is_adult(19) is True

# vérifie un âge 0, un cas d'erreur
def test_age_0():
    assert is_adult(0) is False

# on test un âge négatif
def test_age_minus_5():
    assert is_adult(-5) is False

# on test un string/ un type incorrect
def test_age_str():
    with pytest.raises(ValueError):
        is_adult("dix-huit")
