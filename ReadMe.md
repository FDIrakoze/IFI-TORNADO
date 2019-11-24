# TP TORNADO

Ce TP a pour but de vous introduire Tornado web Framework dans le cadre du cours IFI.


## Première application

Nous avons vu la structure typique d'une application web avec Tornado. (cf Diapo page 12) 

Maintenant, Nous allons essayer de mettre en pratique tout cela ;)!!

  On va vous demander de réaliser votre première application, c'est tout simple:
  
  * Créez une application qui prends en entrée un nombre (le nombre sera récupéré depuis la requête HTTP) et qui affiche un simple message nous disant si le nombre est pair ou impair.


  * Ensuite faite le même exercice mais en utilisant un template html.
  
***`Note: tornado.web.RequestHandler.get_argument()  pourrait vous être utile`***

Si tout se passe bien, vous aurez cela comme résultat:

![result](Capture.PNG)

## REST API

Tornado peut être aussi utilisé pour développer des applications REST. Nous allons donc apprendre  
à travers cette exercice comment developper une API REST.


***`Note: Afin de tester notre API nous allons utiliser un client REST: POSTMAN ou CURL`***

Description:

Nous allons utliser Tornado pour gérer l'ajout et la suppression d'item dans un dictionnaire (type de structure de données dans python) d'items.

Pour ce faire vous avez à disposition un fichier items.py que vous allez devoir compléter pour faire fonctionner l'API.

Les items seront sous format JSON:
```
{
  "id":1,
  "name": "blabla"
}
```

Il va falloir récupérer le JSon dans la request.body et l'ajouter au dictionnaire des items.


Il vous est demandé aussi de rajouter un Requesthandler `printItems`pour afficher sur une page les items dans le dictionnaire.