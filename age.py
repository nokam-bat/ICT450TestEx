# créer la fonction
def is_adult(age):
    if not isinstance(age, int):
        raise ValueError("L'âge doit être un entier.")
    if age >= 18:
        return True
    else:
        return False
