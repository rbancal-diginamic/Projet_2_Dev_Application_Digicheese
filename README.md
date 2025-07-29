# 🧀 DigiCheese

DigiCheese est un projet numérique innovant ayant pour but de refondre un Système d'Information vieillissant, 
permettant à son exploitant de pouvoir suivre et administrer tous les aspects en lien avec la fidélisation de 
la clientèle. Cette refonte a pour but d'optimiser des process tout en comblant une dette technique, afin d'avoir 
une application stable, facilement maintenable et évolutive, qui ajoute fluidité, accessibilité et visibilité pour
les utilisateurs.

---

## 📚 À propos du projet

Le projet DigiCheese a été lancé pour :

- Reduire les bugs réguliers liés à une forte instabilité de l'application existante.
- Permettre une meilleure maintenance applicative.
- Offrir des possibilités d'évolution de développement.
- Proposer une expérience utilisateur agréable afin de gagner en fluidité, accessibilité et visibilité pour les utilisateurs.

---

## 🚀 Fonctionnalités principales

Voici un aperçu des fonctionnalités prévues ou déjà en place :

### 🛒 Gestion des stocks
- Suivi des produits et des quantités disponibles.
- Alertes automatiques sur les seuils critiques.
- Liaison avec fournisseurs et historique d’entrées/sorties.

### 📊 Statistiques & reporting
- Tableau de bord global de l’activité (utilisateurs, produits, stocks).
- Analyse des tendances de consommation et des produits populaires.
- Exports CSV/Excel pour usage comptable ou analytique.

### 📬 Newsletters & communication
- Création et envoi de newsletters personnalisées.
- Segmentation des destinataires par profil ou préférence.
- Statistiques d’ouverture, de clics et de désabonnement.

### 👤 Gestion des utilisateurs
- Comptes personnels ou professionnels.
- Favoris, commentaires, notes.
- Droits et rôles différenciés (admin, opérateurs, etc).

### 🔧 Fonctions avancées (admin)
- Interface d’administration complète.
- Gestion des fournisseurs, des produits, des utilisateurs et des accès.
- Multilingue, multi-structure (mode SaaS possible).

---

## 🛠️ Technologies utilisées

Le projet s’appuie sur une architecture moderne et évolutive :

### Backend
- FastAPI (Python)
- Pydantic de SQLModel pour la validation des données

### Base de données
- MariaDB
- SQLModel basé SQLAlchemy pour l’ORM

---

## 🧪 Lancer le projet en local

### Prérequis
- Git
- Python 3.13+
- Environnement SQL (WampServer par exemple avec MariaDB / MySQL)

### Étapes

1. **Cloner le dépôt**
```bash
  git clone https://github.com/rbancal-diginamic/Projet_2_Dev_Application_Digicheese.git
  cd Projet_2_Dev_Application_Digicheese
```

2. **Installer le projet**
```python
    python -m venv .venv
    pip install -r ./requirements.txt
```

3. **Paramétrer le .env**

- Il faut renseigner les informations permettant de se connecter à une base de données MariaDB créé antérieurement.

4. **Lancer le projet**

Il existe deux façons de lancer le projet :
```python
    - uvicorn src.main:app --port 8000 --reload

    - python run.py
```

5. **Lancer les tests**
```python
    - pytest

    - pytest .\tests

    - pytest .\tests\test_client.py
```
