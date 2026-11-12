# Étape 1 - créer la fonction is_adulte(age) qui retourne True si age>=18 ou False

def is_adult(age):
    """
    Détermine si une personne est majeure.
    :param age: âge en années (entier)
    :return: True si adulte, False sinon
    """
    if not isinstance(age, int): # va vérifier que age est un entier
        raise ValueError("L'âge doit être un entier.")
    if age < 0: # vérifie si le chiffre est négatif pour renvoyer Faux.
        return False
    return age >= 18


if __name__ == "__main__":
    # Boucle interactive avec l'utilisateur
    while True:
        user_input = input("Entrez votre âge (ou 'q' pour quitter) : ")

        if user_input.lower() == "q": # prends en compte maj et min
            print("Au revoir !")
            break

        try:
            age = int(user_input)
            if is_adult(age):
                print("Vous êtes majeur(e).")
            else:
                print("Vous êtes mineur(e).")
        except ValueError:
            print("Veuillez entrer un âge valide (nombre entier).")
