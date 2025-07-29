2025-d04-digicheese/
|---.venv/                                      # Environnement virtuel de chaque personne
|
|---annexes/                                    # Fichiers données SQL
|
|---docs/
|   |--- architecture.md                        #description architecture application
|   |--- endpoint.md                            #
|   |--- scenarii_de_test.md                    #
|
|---img/
|   |--- logo-diginami.png                      #logo entreprise
|
|---src/
|   |--- models/                                #
|        |---__init__.py                        #Fichier init ...   
|        |--- bases/                            #Base pour les schémas et models de l'entité "nomtable"
|             |---__init__.py                   #Fichier init ...
|             |---"nomtable".py                 #
|        |--- db_models/                        #Schéma de la table "nomtable" représentée en base de données
|             |---__init__.py                   #Fichier init ...
|             |---"nomtable"_db.py              #
|        |--- schemas/                          #
|             |---__init__.py                   #Fichier init ...
|             |---"nomtable"/                   #
|                 |---__init__.py               #Fichier init ...
|                 |---"nomtable"_patch.py       #Schéma "nomtable" pour modification en base de données
|                 |---"nomtable"_post.py        #Schéma "nomtable" pour création en base de données
|
|   |--- repositories/                          #
|        |---__init__.py                        #Fichier init ...
|        |---abstract_repository.py             #
|        |---__init__.py                        #Fichier init ...
|
|   |--- routers/                               #
|        |---__init__.py                        #Fichier init ...
|        |---"nomtable"_subrouteur.py           #Repository for managing "nomtable"" entities in the database.
|
|   |---services/                               #
|       |---__init__.py                         #Fichier init ...
|       |---"nomtable"_service.py               #Service to do treatments on "nomtable"" entities before commit in database.
|   |---database.py                             #
|   |---main.py                                 #
|   |---old_models.py                           #
|
|---script/                                    # Emplacement script SQL 
|
|---tests/                                      #
|   |---__init__.py                             #Fichier init ...
|   |---conftest.py                             #
|   |---test_"nomtable".py                      #Fichier test "nomtable"
|
|---.env                                        #Variables d’environnement
|---.env-template                               #Environnement virtuel Python template
|---.gitignore                                  #fichiers ignorés
|---Projet_Sujet.pdf                            #ancien README .pdf   
|---requirement.txt                             #Dépendances Python du projet
|---run.py                                      #
|---test_main.http                              #
|---Readme.md                                   #
|
