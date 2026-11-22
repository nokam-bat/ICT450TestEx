le prof a crée une `classe` qui sert à créer une petite fiche utilisateur qui contient un email.

**explication du code du prof**
`class Utlisateur` : définit le modèle de la fiche
`__init__()` : s'exécute automatiquement quand on crée un utilisateur.
`self` : représente l'utilisateur/ l'objet qu'on est entrain de créer (d'initialiser). c'est un objet/paramètre fourni par Python dans la fonction native `__init__(self, )`.

`self.email` : c'est l'info conservée dans l'utilisateur.
`self.email = email` : enrengistre l'email reçu dans sa fiche.
=> **Donc le prof garde que email et pas mdp donc on va juste checker email dans les tests**


`email.split('@')` : découpe le texte de l'email à l'endroit du `@`.
`[-1]` : récupère le dernier morceau de la liste. 
*explication des positions des éléments* : avec une liste comme exemple ; 
`liste = ["léa", "exemple", "com"]`
* `[0]` : léa
* `[1]` : exemple
* `[-1]` : com (dernier élément)

Dans le cas de `["léa", "exemple.com"]` : 
* `liste[1]` : exemple (deuxième élément)
* `liste[-1]` : com (dernier élément.)
=> le deuxième élément est aussi le dernier.
* 

db=None veut dire qu'on peut appeler la fonction sans BD
la fonction retourne un objet Utilisateur dont on peu lire l'email avec resultat.email.


`if db is not None` : si une BD a été fournie.

## **dans test_inscriptionUtilisateur.py** pour l'exercice avec le Mock
pour simuler un test d'email déjà utilisé, on utilise un objet factice `mock` qui jouera le rôle de la BD.
`from unittest.mock import Mock` : importe un objet factice.

`db = Mock()` : on le stock dans db
`db.email_existe.return_value = True` : dans le code du prof y'a db.email_existe(email). donc on fait le test en conséquence.
`return_value` : c'est un attribut des objets Mocks fournit par le module.

## `db.email_existe.return_value = True`
* `db` : le faux objet qui représente la BD
* `.email_existe` : la méthode simulée à laquelle on s'intéresse. (dans le code du prof c'est db.email_existe(email))
* `.return_value` : sa réponse lorsqu'elle sera appelée
* `= True` : on choisit cette réponse

`.` : le point permet d'accéder à qqc appartenant à un objet.

Pour ce test on va utiliser les paramètres email, mdp et db