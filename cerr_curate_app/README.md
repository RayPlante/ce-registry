# CERR Curation CDCS App

This directory contains a CDCS plug-in Django app that provides a customized form for
creating and editing recrods.

## Prerequisites

 * Python 3.5
 * Django ...
 * CERR   ... (not needed for standalone demonstration)


## Demonstrating as a standalone app

Currently, the editing process can be demonstrated as a standalone app.  To run:

 1.  Change into this directory

 2.  Prep the database:
     ```
     python manage.py migrate
     ```

 3.  Run the server
     ```
     python manage.py migrate
     ```

 4.  With a browser, access `http://127.0.0.1:8000/draft/start
