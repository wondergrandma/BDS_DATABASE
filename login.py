import logging
import psycopg2
from tkinter import *
import bcrypt

#Premené pre pripojenie aplikácie k PG admin
DB_HOST = "localhost"
DB_NAME = "projekt"
DB_USER = "postgres"
DB_PASS = "postgres"

class Login:

    email = ""
    password = u""

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        
    def comparePasswords(self):
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()

        cur.execute("SELECT pwd FROM \"user\" WHERE mail = %s ", (self.email,))
        hashed = cur.fetchall()
        result = hashed[0][0]

        conn.commit()
        cur.close()

        if bcrypt.checkpw(self.password.encode(), result):
            return True
        else:
            return False    