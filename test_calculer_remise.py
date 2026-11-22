from calculer_remise import calculerRemise
import pytest

# cas standard _ un client fidèle effectue un achat avec un total positif
def test_calculer_remise_standard():
    # Arrange
    total = 100
    clientFidele = True

    # Act
    result = calculerRemise(total, clientFidele)

    # Assert
    assert result == 90

# cas limite : total à 0, client fidele ou non
def test_calculer_remise_zero():
    # arrange
    total = 0
    clientFidele = False

    # act
    result = calculerRemise(total, clientFidele)

    # assert
    assert result == 0


# cas d'erreur : total négatif avec exception ValueError
def test_calculer_remise_negatif():
    # arrange
    total = -10
    clientFidel = True

    # act and assert
    with pytest.raises(ValueError):
        calculerRemise(total, clientFidel)

