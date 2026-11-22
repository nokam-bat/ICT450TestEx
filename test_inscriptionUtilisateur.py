from inscriptionUtilisateur import inscriptionUtilisateur
import pytest
# pour simuler une BD on va utiliser un faux objet Mock qui jouera le rôle de la BD.
from unittest.mock import Mock


# email et mot de passe valide
def test_inscription_valid():
    # Arrange
    email = "noor@gmail.com"
    mdp = "miaoumiaou"

    # Act
    result = inscriptionUtilisateur(email, mdp)

    # Assert
    # le code du prof ne garde que l'email dans l'objet retourné (self.email=email) donc on check que l'email
    assert result.email == email

# email invalide
def test_inscription_invalid():

    # Arrange
    email = "utilisateur.com"
    mdp = "miaoumiaou"

    # Act & Assert
    with pytest.raises(ValueError):
        inscriptionUtilisateur(email,mdp)

# mot de passe trop court
def test_inscription_short_mdp():
    # Arrange
    email = "noor@gmail.com"
    mdp = "miaou"

    # Act and Assert
    with pytest.raises(ValueError):
        inscriptionUtilisateur(email, mdp)

# email déjà utilisé (en utilisant nu simulateur de BD)
def test_inscription_used_email():
    #Arrange
    email = "noor@gmail.com"
    mdp = "miaoumiaou"
    db = Mock()
    db.email_existe.return_value = True

    # Act and Assert
    with pytest.raises(ValueError):
        inscriptionUtilisateur(email, mdp, db)

# l'email de type incorrecte, donc ce sera pas du texte
def test_inscription_wrong_type_email():
    # Arrange
    email = None
    mdp = "miaoumiaou"

    # Act and Assert
    with pytest.raises(TypeError):
        inscriptionUtilisateur(email, mdp)