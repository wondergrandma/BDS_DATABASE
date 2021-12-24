# BDS_DATABASE
```
Application can be built from command line. 
The goal of the application is that the user can check inforamtions about users in database.
User can add, delete and update user in database. Also can use tool for searching.
```
```
 def sql_injection():
            find_data = dummy_box.get()
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()
```
## External libraries

```
Bcrypt
Psycopg2
```
