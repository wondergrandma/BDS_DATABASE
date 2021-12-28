# BDS_DATABASE

Application can be run in Visual Studio. 

The goal of the application is that the user can check inforamtions about users in database.

User can add, delete and update users in database. Also can use tool for searching.

All added passwords are hashed using hash algorithm provided by bcrypt library.

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

Application is also able to trac who used which command and what was writen in Entry boxes this tracking is provided by logger.

All informations are printed in seppared file "activity_log.log" - this file is ignored by .gitignore.

Exaple of logger code:

```

```

Licenses were generated using `$ pip install pip-licenses` and `$ pip-licenses --format=plain-vertical`

## Check list

Pwd's in hash format -- DONE

Sign up window with pwd authentication --

User role and new schema -- DONE

CRUD -- DONE

JOIN -- DONE

Transactions -- DONE

Filtering data -- DONE

Dummy table for SQL injection testing -- DONE

Backupping database every midnight -- 

Log -- DONE

Gitrepositary with README file and .gitignore -- DONE

Add licenses -- DONE

SSH key -- DONE

## External libraries


Bcrypt

Psycopg2
