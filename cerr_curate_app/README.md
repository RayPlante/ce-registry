# CERR Curation CDCS App

This directory contains a CDCS plug-in Django app that provides a customized form for
creating and editing recrods.

## Prerequisites

 * Python 3.5
 * Django ...
 * CERR   ... (not needed for standalone demonstration)
 * Docker and docker-compose ... (needed for the standalone demonstration)


## Demonstrating as a standalone app

Currently, the editing process can be demonstrated as a standalone app.  To run:

 1.  Change into this directory

 2.  Start the MongoDB database via Docker
     1. temporarily change into the `docker` subdirectory
     2. type: `inenv.sh docker-compose up -d`
     3. if desired, visit http://localhost:8081 to see the contents of the database (via Mongo Express)
     4. return to the parent directory

 3.  Prep the database:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

 4.  Run the server
     ```
     python manage.py runserver 127.0.0.1:8000
     ```

 4.  With a browser, access `http://127.0.0.1:8000/draft/start

