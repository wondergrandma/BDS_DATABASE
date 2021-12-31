# BDS_DATABASE

Application can be run in Visual Studio also as .exe file on Windows. 

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

Creating logger:

```
logging.basicConfig(
level=logging.INFO,
format= "{asctime} {levelname:<8} {message}",
style='{',
filename='activity_log.log',
filemode='a'
)
```

Example of logger code:

```
logging.info('Showing database data to user: ' +email)
```

Licenses were generated using `$ pip install pip-licenses` and `$ pip-licenses --format=plain-vertical --with-license-file`.

Application was build using external library Pyinstaller using `$ pip3 install pyinstaller` and for building `$ pyinstaller main_gui.py` 

## External libraries


Bcrypt

Psycopg2

Pyinstaller
