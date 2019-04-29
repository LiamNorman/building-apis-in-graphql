# building-apis-in-graphql

Talk and codebase for Building APIs in GraphQL Presentation

## Dependencies

Ensure you have the following dependencies:

* [Python >= 3.7](https://www.python.org/downloads/) 
* [pip >= 19.03](https://pip.pypa.io/en/stable/installing/)
* [GraphiQL Client](https://electronjs.org/apps/graphiql)
* [SQLite3](http://www.sqlitetutorial.net/download-install-sqlite/)

## Installation

```bash
source ~/venv/bin/activate
pip install django==2.1.4 graphene-django==2.2.0 django-filter==2.0.0 django-graphql-jwt==0.1.5
cd /yourproject/graphpod
python manage.py migrate
python manage.py runserver
```

## Slides
The presentation can be found in the `slides/` folder


## Queries

All queries are stored in `graphpod/queries.graphql`

## Schema 

Schema design is stored in `graphpod/designedschema.graphql`

## Logging in as a User
Please refer to the queries.graphql to see how to authenticate. Run the createUser and tokenAuth mutations to get the token of your user. Once you have obtained the token, you will
have to alter your headers in the GraphiQL client. As an example, you would set the `Authentication` header key to
`JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...`

## Database 
You can view the database at ```graphpod/graphpoddb.sqlite3``` using a SQLite Database Viewer such as SQLite Browser
