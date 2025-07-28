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
|        |--- bases/                            #
|             |---__init__.py                   #
|             |---"nomtable".py                 #
|        |--- db_models/                        #
|             |---__init__.py                   #
|             |---"nomtable"_db.py              #
|        |--- schemas/                          #
|             |---__init__.py                   #
|             |---"nomtable"/                   #
|                 |---__init__.py
|                 |---"nomtable"_patch.py
|                 |---"nomtable"_post.py
|
|   |--- repositories/                          #Point d'entrée FastAPI
|        |---__init__.py                        #Point d'entrée FastAPI
|        |---abstract_repository.py             #
|        |---__init__.py
|
|   |--- routers/                               #Point d'entrée FastAPI
|        |---__init__.py
|        |---"nomtable"_subrouteur.py
|
|   |---services/
|       |---database.py
|       |---main.py
|       |---old_models.py
|
|---script/                                    # Emplacement script SQL 
|
|---tests/
|   |---__init__.py
|   |---conftest.py
|   |---test_"nomtable".py
|
|---.env
|---.env-template
|---.gitignore
|---README.pdf
|---requirement.txt
|---run.py
|---test_main.http
|
