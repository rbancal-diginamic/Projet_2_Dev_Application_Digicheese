2025-d04-digicheese/
|---.venv/                                      # Environnement virtuel de chaque personne
|
|---annexes/                                    # Fichiers données SQL
|
|---docs/
|   |--- architecture.md                        # Description architecture application
|   |--- endpoint.md                            # Description des différents Endpoints de l'application
|   |--- scenarii_de_test.md                    # Explicatifs des tests associés aux différents Endpoints
|
|---img/
|   |--- logo-diginami.png                      # Logo entreprise
|
|---src/
|   |--- models/                                #
|        |---__init__.py                        # Fichier init ...   
|        |--- bases/                            # Base pour les schémas et models de l'entité "nomtable"
|             |---__init__.py                   # Fichier init ...
|             |---"nomtable".py                 #
|        |--- db_models/                        # Models de la table "nomtable" représentée en base de données
|             |---__init__.py                   # Fichier init ...
|             |---"nomtable"_db.py              #
|        |--- schemas/                          # Schémas pour valider les données envoyées en post / patch
|             |---__init__.py                   # Fichier init ...
|             |---"nomtable"/                   #
|                 |---__init__.py               # Fichier init ...
|                 |---"nomtable"_patch.py       # Schéma "nomtable" pour modification en base de données
|                 |---"nomtable"_post.py        # Schéma "nomtable" pour création en base de données
|
|   |--- repositories/                          #
|        |---__init__.py                        # Fichier init ...
|        |---abstract_repository.py             # Repository abstrait pour cadrer les repositories des classes
|        |---__init__.py                        # Fichier init ...
|
|   |--- routers/                               #
|        |---__init__.py                        # Fichier init ...
|        |---"nomtable"_subrouteur.py           # Repository for managing "nomtable"" entities in the database.
|
|   |---services/                               #
|       |---__init__.py                         # Fichier init ...
|       |---"nomtable"_service.py               # Service to do treatments on "nomtable"" entities before commit in database.
|   |---database.py                             # Fichier de configuration de la BDD
|   |---main.py                                 # Fichier principal de l'application
|   |---old_models.py                           # Anciens modèles de la BDD
|
|---script/                                     # Emplacement script SQL 
|
|---tests/                                      #
|   |---__init__.py                             # Fichier init ...
|   |---conftest.py                             # Fichier de configuration de l'environnement de tests
|   |---test_"nomtable".py                      # Fichier test "nomtable"
|
|---.env                                        # Variables d’environnement à configurer en local avec .env.template
|---.env.template                               # Environnement virtuel Python template
|---.gitignore                                  # Fichiers ignorés
|---Projet_Sujet.pdf                            # Ancien README.pdf   
|---requirement.txt                             # Dépendances Python du projet
|---run.py                                      # Fichier de lancement du projet
|---test_main.http                              #
|---Readme.md                                   # Explication Projet avec installation et utilisation
|
