# Projet ETL : Analyse des Salaires Municipaux de Boston

## Objectif du projet 📘
Le but ici est simple : créer un pipeline ETL (Extraction, Transformation, Chargement) automatisé pour analyser les salaires des employés municipaux de la ville de Boston. Une fois les données lavées , on pourra les analyser tranquillement dans un fichier bien agencé et propre.

---

## Backlog Produit 🧱
Le projet s'articule autour de quatre grandes étapes : 

1. **Extraction des données** (via une API)  
   Nous commencons par récupérer les données brutes depuis l'API Boston Open Data.

2. **Transformation des données** (nettoyage)  
   Une fois les données extraites, il faut les transformer : enlever les doublons, gérer les valeurs manquantes, et ajuster les formats de données.

3. **Chargement des données** (format CSV)  
   Une fois les données prêtes et lavées, nous les chargeons dans un fichier CSV. Cela permet de les analyser plus facilement.

4. **Analyse des données** (statistiques)  
   Après le nettoyage et le chargement, nous pouvons les analyser tranquillement.

---

## Rôles et Processus 👥

- **Product Owner** : Fergal
  
- **L'équipe** : Thomas-Idriss-Samuel-Enoque ( Membres de l'équipe )    

- **Échanges** :
  Messages via Teams ou Discord pour s'organiser - discuter de l'avancement du projet. 
  

---

## Organisation des Sprints 🕒
Le projet est divisé en 4 sprints, un pour chaque étape du pipeline. Voici ce à quoi cela ressemble :

| **Sprint**   |   **Objectif**             | Durée                 |
|--------------|----------------------------|-----------------------|
| **Sprint 1** | Extraction des données     | 09/10/2025-15/10/2025 |
| **Sprint 2** | Transformation des données | 14/10/2025-15/10/2025 |
| **Sprint 3** | Chargement dans un CSV     | 14/10/2025-15/10/2025 |
| **Sprint 4** | Analyse des données        | 15/10/2025-15/10/2025 |


Technologies utilisées 📊

Voici les principaux outils qu'on a utilisé sur ce projet :

    Python : Le langage principal pour implémenter le pipeline ETL.

    Pandas : La bibliothèque pour manipuler et nettoyer les données.

    Requests : Pour récupérer les données de l'API.

    Matplotlib : Pour générer des graphiques et visualiser les statistiques des salaires.
