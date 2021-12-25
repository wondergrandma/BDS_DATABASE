# BDS_DATABASE

Application can be built from command line. 

The goal of the application is that the user can check inforamtions about users in database.

User can add, delete and update user in database. Also can use tool for searching.

Connection to PG admin database is provided by code down below and external library Psycopg2.

```
DB_HOST = "localhost"
DB_NAME = "projekt"
DB_USER = "postgres"
DB_PASS = "postgres"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
```

After executing this code the application is able to execute PostgreSQL commands in python format such as:

```
cur.execute("SELECT user_id, first_name, second_name, mail, pwd FROM \"user\" WHERE second_name = %s ", (find_data,))
```

## Check list

Pwd's in hash format -- DONE

Sign up window with pwd authentication --

User role and new schema --

CRUD -- DONE

JOIN -- 

Transactions -- DONE

Filtering data -- DONE

Dummy table for SQL injection testing -- DONE

Backupping database every midnight -- 

Log -- 

Gitrepositary with README file and .gitignore -- DONE

Add licenses -- DONE

## External libraries


Bcrypt

Psycopg2
