# TP TORNADO

Ce TP a pour but de vous introduire Tornado web Framework dans le cadre du cours IFI.

## Initialisation de l'environnement
Création de votre environnement virtuel : `virtualenv env_name -p python3`

Activation de votre environnement virtuel : `source env_name/bin/activate`

Toutes les commandes utiles devront maintenant être exécutées avec l'environment virtuel actif.

Pour sortir de l'environnement virtuel `deactivate`

Installation de Tornado dans l'environnement virtuel : `pip3 install tornado`


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


## NEWS 

L'objectif de cet exercice est d'afficher une liste d'articles récupérés depuis une api : "https://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey=9e1d0b0198fa42f8b8966332df05b8ed"    

L'arborescence de l'exercice : 
    - un fichier python "article.py"
    - un dossier templates comprenant : "index.html", "article.html"

### Récupération des articles 
Dans un premier temps, on cherche à récuperer la liste d'articles depuis l'api, pour ce faire il sera donc nécessaire d'implementer un RequesHandler : 'MainHandler'

L'api vous retournera un json, concernant les détail de ça structure : https://newsapi.org/ 

**PS : Vous aurez peut être besoin d'utilisez une/des méthodes asynchrones**

### Affichage des articles
Dans un second temps, on cherche à afficher les articles récupérés précédemment, vous aurez donc besoin d'utilisez un template ('index.html'). 
Vous aurez pour missions, si vous l'acceptez d'afficher une liste d'article. Voici, un aperçu final :     
![result](article_list_rendu.PNG)


**PS : vous pouvez reprendre le code htlml fournis dans "base.html" pour l'utilisation de bootstrap, ou utiliser vos propre fichier css auquel cas il faudra les importer au projet**   
certaines urls utiles pour bootstrap :    
    https://getbootstrap.com/docs/4.0/layout/media-object/      
    https://getbootstrap.com/docs/4.0/content/images/   
    https://getbootstrap.com/docs/4.0/utilities/sizing/   
    
### More Info 
Maintenant que la liste d'articles s'affiche correctement, on souhaite pouvoir accéder à d'avantages d'informations sur un article précis, comme on peut le constater sur la dernière image : "More Info". Pour cela, il va falloir implémenter un nouvel RequestHandler, appeler le "ArticleDetailHandler". 
Vous aurez donc besoin de stocker la liste d'articles que vous aviez récupérer dans le 'MainHandler', même si il existe sûrement d'autres moyen de stocker cette liste, dans le notre on ce contentera d'une variable global.

Afin de récupérer un article précis, vous aurez sûrement besoin d'un indice. Celui-ci devrait normalement être implementer dans le template comme une variable locale.

Une fois toutes ces étapes faites, il ne vous reste plus qu'à implémenter votre classe "ArticleDetailHandler".

Petite aperçu de ce qui est souhaité :   
![result](more_info_rendu.PNG)

### Pour aller plus loin 
Nous avons maintenant envie, de récupérer des informations provenant de différentes api. 

API :  "https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=9e1d0b0198fa42f8b8966332df05b8ed", "https://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey=9e1d0b0198fa42f8b8966332df05b8ed"

Modifier le fichiers article.py, pour qu'il puisse récupérer et afficher ces informations
