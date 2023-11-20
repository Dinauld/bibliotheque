# Gestion de Bibliothèque

Ce script Python offre une gestion simple d'une bibliothèque avec une interface graphique basée sur Tkinter et utilise une base de données SQLite pour stocker les informations sur les livres, les utilisateurs et les prêts.

## Configuration initiale

Avant d'utiliser le script, assurez-vous d'avoir les prérequis suivants installés sur votre système :
- Python (version 3.x)
- Tkinter (généralement inclus avec Python)

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Dinauld/bibliotheque.git
   cd votre-repo

    Assurez-vous d'avoir une base de données SQLite (bibliotheque.db dans cet exemple) dans le même répertoire que le script. Si elle n'existe pas, le script la créera automatiquement avec les tables nécessaires.

## Utilisation

    Exécutez le script en utilisant la commande suivante :

    bash

    python script.py

    L'interface graphique s'ouvrira, vous permettant d'ajouter des livres à la bibliothèque en fournissant le titre, l'auteur, le genre et l'ISBN.

    Vous pouvez également afficher tous les livres actuellement dans la base de données en appuyant sur le bouton "Afficher Livres".

## Fonctionnalités

    Ajouter un livre : Remplissez les informations nécessaires dans les champs d'entrée, puis appuyez sur le bouton "Ajouter Livre". Les données seront enregistrées dans la base de données.

    Afficher les livres : Appuyez sur le bouton "Afficher Livres" pour afficher tous les livres présents dans la base de données.

## Notes

    Les tables de la base de données (Livres, Utilisateurs, Prets) sont créées automatiquement si elles n'existent pas déjà.

    Les dates d'emprunt et de retour des livres ne sont pas encore implémentées dans cet exemple.