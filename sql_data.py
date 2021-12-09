import psycopg2

DB_HOST = "localhost"
DB_NAME = "projekt"
DB_USER = "postgres"
DB_PASS = "postgres"

#Struktura funkcie
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()


cur.execute("SELECT iban FROM account")
conn.commit()
ahoj = cur.fetchall()

cur.close()
conn.close()

"""for i in ahoj:
    print(i)"""

class Sql:

    def loginSql(window):
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()

        cur.execute("SELECT pwd FROM users WHERE mail")

        conn.commit()
        cur.fetchall()
        cur.close()
        conn.close()
