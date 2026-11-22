# test_inscriptionUtilisateur.py

import pytest
from unittest.mock import Mock


# --- Code à tester ---

class Utilisateur:
    def __init__(self, email):
        self.email = email


# db=None veut dire qu'on peut appeler la fonction sans BD
# la fonction retourne un objet Utilisateur dont on peu lire l'email avec resultat.email.

def inscriptionUtilisateur(email, motDePasse, db=None):
    """
    Fonction qui simule l'inscription d'un utilisateur.
    - email : chaîne de caractères
    - motDePasse : chaîne de caractères
    - db : interface simulée avec méthode email_existe(email)

    Lève ValueError ou TypeError selon les cas.
    Retourne un objet Utilisateur en cas de succès.
    """

    # Vérifications basiques
    if not isinstance(email, str):
        raise TypeError("L'email doit être une chaîne de caractères")
    if not isinstance(motDePasse, str):
        raise TypeError("Le mot de passe doit être une chaîne de caractères")
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise ValueError("Email invalide")
    if len(motDePasse) < 8:
        raise ValueError("Mot de passe trop court")

    # Vérification base de données simulée
    # vérifie si l'email est déjà utilisé
    if db is not None and db.email_existe(email):
        raise ValueError("Email déjà utilisé")

    # Succès : création de l'utilisateur
    return Utilisateur(email)
