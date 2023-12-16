# Implémentez un modèle de scoring
## Présentation
* La mission principale de ce projet est de prédire le risque de faillite d'un client pour une société de crédit. Pour cela, nous devons configurer un modèle de classification binaire et d'en analyser les différentes métriques.

* Ce projet consiste à créer une API web avec un Dashboard interactif. Celui-ci devra a minima contenir les fonctionnalités suivantes :

1. Permettre de visualiser le score et l’interprétation de ce score pour chaque client de façon intelligible pour une personne non experte en data science.
2. Permettre de visualiser des informations descriptives relatives à un client.
4. Permettre de comparer les informations descriptives relatives à un client à l’ensemble des clients ou à un groupe de clients similaires.

* Dans ce repository , vous trouverez :

- Un dossier **Modélisation** contenant toirs notebook Jupyter pour l'anlyse des donnés, l'entraînement et la configuration du modèle de classification ainsi que l'imortance des features et la fontion coût.
- Un dossier **API** contenant le fichier api_home_risk.py qui est le fichier Flask contenant la partie backend.
- Un dossier **Dashboard** contenant le fichier **dashboard_dev**  qui représente la partie Frontend codée avec Streamlit. 
- La note technique qui explique en détails la construction et les résultats du modèle.
_ La présentation ppt

## Dashboard / API
* J'ai utilisé deux librairies Python pour ce sujet :

1. Flask
2. Streamlit

Il est déployé sur Heroku ici  : https://dashboard-oc-p7.herokuapp.com/
