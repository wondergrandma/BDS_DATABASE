import psycopg2

DB_HOST = "localhost"
DB_NAME = ""
DB_USER = "postgres"
DB_PASS = "postgres"

#Struktura funkcie
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

cur.execute("")
conn.commit()

cur.close()
conn.close()