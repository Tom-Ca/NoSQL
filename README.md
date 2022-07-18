Suivre les indications pour se créer un compte developeurs Fitbit :
https://dev.fitbit.com/build/reference/web-api/developer-guide/getting-started/
https://dev.fitbit.com/build/reference/web-api/developer-guide/authorization/

A partir de l'étape 3 : 

- récupérer la fin de l'URL
- Le metre ligne 17 de get token.py
- Lancer le fichier get token.py
- Récupérer la sortie et remplir tokens.txt

Pour finir de setup fitbit, remplire le fichier get_token.py

Pour lancer en local:

    Installer et lancer mongodb en local
    Décomenter la ligne 266 de main.py
    Comenter la ligne 268 de main.py
    Lancer le programme et suivre les indications.
    
Pour lancer sur atlas :
    
    Créer bdd sur atlas
    Décomenter la ligne 268 de main.py
    Y mettre le lien vers votre bdd atlas
    Comenter la ligne 266 de main.py
    Lancer le programme et suivre les indications.

Pour la visualisation en locale:
    
    Installer : BI Connector
    Installer : MongoDB BI Connector ODBC Driver
    Suivre : https://www.mongodb.com/docs/bi-connector/current/tutorial/create-system-dsn/
    Ouvrir le fichier '.pbix'
    Puis suivre ce tuto : https://www.mongodb.com/docs/bi-connector/current/connect/powerbi/

Pour la visualisation sur Atlas :
    
    Il faut payer un serveur et suivre ce tuto:
        https://www.mongodb.com/docs/atlas/tutorial/connect-bic-powerbi/

Trello : https://trello.com/invite/b/1LfgR9DQ/b270a4ebc4300bf671f4a7142bfbaaa1/projet-nosql
Support de Présentation : https://docs.google.com/presentation/d/1-C2mx_BiTuZnghhbb6bMR9wgjUVEVIXyEoeYZJbhfuk/edit?usp=sharing
Support de Présentation : https://docs.google.com/presentation/d/1-C2mx_BiTuZnghhbb6bMR9wgjUVEVIXyEoeYZJbhfuk/edit?usp=sharing