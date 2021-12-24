# BDS_DATABASE

Application can be built from command line. 

The goal of the application is that the user can check inforamtions about users in database.

User can add, delete and update user in database. Also can use tool for searching.

Connection tu PG admin database is provided by code down below.

```
DB_HOST = "localhost"
DB_NAME = "projekt"
DB_USER = "postgres"
DB_PASS = "postgres"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
```
## External libraries


Bcrypt

Psycopg2

