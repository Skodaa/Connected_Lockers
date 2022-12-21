# Projet de casiers connectés

Ce projet à pour but de mettre en place une base de données ainsi que les moyens de l'utiliser dans le but de créer une baie de casiers connectés, pour ce faire nous allons retrouvé différents éléments notamment, un serveur réseau en python, un client réseau en JAVA, mais aussi un site web héberger sur alwaysdata.

## Prérequis : 

Pour utiliser le serveur python vous devrez posséder une version relativement récente de python (python3 est un minimum)
vous devrez aussi posseder une bibliothèque externe nommée psycopg2 que vous devrez avoir installé au préalable.

pour ce faire vous pourrez simplement taper dans votre terminal :

    pip install psycopg2

ou alors l'installer directement sur ce lien : <https://pypi.org/project/psycopg2/#files>

vous pouvez retrouver la documentation de cette bibliothèque ici : <https://www.psycopg.org/docs/>

nous utilisons aussi une bibliothèque déjà présente dans python du nom de socket, dont vous pouvez trouver la documentation en cliquant sur ce lien : <https://docs.python.org/3/library/socket.html>

## Utilisation :

De base les adresses ip du serveur et du client est "127.0.0.1" mais c'elle ci sont modifiable, tout comme les ports, de bases le port écouté est 50001 mais est modifiable.

Le serveur n'as besoin d'être lancée qu'une seul fois pour être utilisé, il resteras en écoute continuellement.
Le client cependant sera lancé pour chaque utilisation dans une optique de ne pas créer d'erreur de connexion sur le long terme.

pour accéder aux services de nos casier, vous devrez initialement être présent dans notre base de données afin de ne permettra qu'aux utilisateurs de l'université d'acceder aux casiers par exemple.

### Client

Le client est utilisable en suivant un certain schema :

lors du lancement du client, si une carte administrateur est reconnu, alors les informations qu'elle contient sont automatiquement enregistré dans le client. sinon le client va chercher à se connecter à un serveur sur l'adresse et le port enregistrer de base.

s'il arrive à se connecter, il enverras un message pour identifier l'utilisteur, de la forme : 
    [numéro d'utilisateur],[numéro de la carte]

si l'authentification réussi, il enverra la commande à effectuer ainsi que le casier sur lequel l'effectuer :

    [id casier],[open/close]

et enfin si l'échange est terminé ou si l'utilisateur n'est pas reconnu, le casier envoi un message pour terminer la connection :

    close_connection

Si jamais le client ou le serveur mettent trop de temps, l'un comme l'autre coupe la connexion dans un delais prédéfinis.

### Site web

notre site web héberger sur alwaysdata : <volquardsen.alwaysdata.net>

ici encore l'utilisateur devra s'identifier avant de pouvoir accéder aux services de notre site.
Si l'utilisateur n'as jamais activer sont compte, il devra le faire en rentrant sont numéro d'utilisateur ainsi qu'en créant un mot de passe, il pourras ensuite se connecter et utiliser le site.