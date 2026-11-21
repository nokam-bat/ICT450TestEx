from prix import calculer_prix_ttc
import pytest

def test_calculer_prix_ttc_standard():
    # Arrange : prépare les données
    prix_ht = 100
    tva = 0.2

    # Act : appeler la fonction importée à tester (calculer_prix_ttc)
    resultat = calculer_prix_ttc(prix_ht, tva)

    # Assert : évaluer le résultat
    assert resultat == 120

# vérifie le prix_ht négatif à -50
def test_calculer_prix_ttc_prix_negatif():
    # Arrange
    prix_ht = -50
    tva = 0.2

    #Act + Assert
    with pytest.raises(ValueError): # vérifie que l'appel déclenche une ValueError
        calculer_prix_ttc(prix_ht, tva)


# vérifie que la tva est négative à -0.2
def test_calculer_prix_ttc_tva_negatif():
    # Arrange
    prix_ht = 100
    tva = -0.2

    # Act et Assert
    with pytest.raises(ValueError):
        calculer_prix_ttc(prix_ht, tva)


# vérifie un cas limite où le prix est à 0. (autorisé)
def test_calculer_prix_ttc_prix_zero():
    # Arrange
    prix_ht = 0
    tva = 0.2

    # Act
    resultat = calculer_prix_ttc(prix_ht, tva)
    # Assert (devrait renvoyer 0.0)
    assert resultat == 0.0

# vérifie un type string (invalide) et ça doit lever un TypeError
def test_calculer_prix_ttc_str():
    # Arrange
    prix_ht = "cent"
    tva = 0.2

    # Act and Assert
    with pytest.raises(TypeError):
        calculer_prix_ttc(prix_ht, tva)