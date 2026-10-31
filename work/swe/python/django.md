
Python framework for backend. Includes features out of the box like a login system, database connection, and CRUD operations (Create Read Update Delete).

Follows the MVT pattern (Model, View, Template). 

## Definitions

**Model**
A model usually provides data from the database. We generally use SQL to query data from a database, but it is possible to use Django (with object relational mapping, ORM) to communicate with the database. Models are usually located within a file called `models.py`.


**View**
A function/method that takes http requests as arguments, imports models, finds data to send to the template, and returns the final result. Views are usually located within a file called `views.py`.


**Template**
A file that describes how the result should be represented (usually HTML). Templates are usually located in a folder called `templates/`


**URLs**
When a user requests a URL, Django decides with view it will send the request to. This logic is handled in `urls.py`.


