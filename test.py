import bcrypt
import psycopg2

heslo = b"ahoj"

hashed_heslo = bcrypt.hashpw(heslo, bcrypt.gensalt())
print(hashed_heslo.decode())



















"""pwd = b"ahoj"

hashed_pwd = bcrypt.hashpw(pwd, bcrypt.gensalt())

print(str(hashed_pwd))
print()

if bcrypt.checkpw(pwd, hashed_pwd):
    print("ANO")
else:
    print("SANEL SMRDI")"""