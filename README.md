## OC_GrandPy_Bot
## Project 7 from the OpenClassrooms's school

## Cahier des charges
### Fonctionnalités
* Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
* Vous utiliserez l'API de Google Maps et celle de Media Wiki.
* Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.
* Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous !

## Comment accéder au site ?
Tout se passe ici https://grandpy-jilvo.herokuapp.com/

## Comment faire marcher le programme ?
Voici les différentes instructions pour faire marcher le programme correctement.
### Installation :
````
pip install -r OC_GrandPy_Bot/requirements.txt
````
#### Utilisation
Lancer le fichier *run.py* contenu dans la racine, puis ouvrir la lien web affiché dans la console *http://localhost:5000/*

Ou aller directement sur ce lien https://grandpy-jilvo.herokuapp.com/

#### Fonctionnement
Le site envoie des requêtes au micro programme qui ensuite passe des *requests* via GoogleMap et MediaWiki pour ensuite renvoyer les reponses et les afficher sur le site.

#### Environnement virtuel
Les librairies necessaires sont trouvables dans le fichier requirements.txt

## Auteur et Contribution:
J'ai développé ce programme dans le cadre d'une formation sur Openclassrooms.

Par conséquent toute pull request avec du code sera refusé. Ouvrez plutôt une issue pour signaler un bug, une faute d'orthographe ou pour simplement donner un conseil.
