import logging
import psycopg2
from tkinter import *
import bcrypt

#Logging
logging.basicConfig(
level=logging.INFO,
format= "{asctime} {levelname:<8} {message}",
style='{',
filename='activity_log.log',
filemode='a'
)

#Premené pre pripojenie aplikácie k PG admin
DB_HOST = "localhost"
DB_NAME = "projekt"
DB_USER = "postgres"
DB_PASS = "postgres"

class Login:

    email = ""
    password = ""

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.hashed = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())
        
    def comparePasswords(self):
        try:
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()

            cur.execute("SELECT pwd FROM \"user\" WHERE mail = %s ", (self.email,))
            hashed = cur.fetchall()
            result = hashed[0][0]

            conn.commit()
            cur.close()

            if bcrypt.checkpw(self.password.encode(), result.encode()):
                return True
            else:
             return False
        except: 
            logging.info('WRONG EMAIL')