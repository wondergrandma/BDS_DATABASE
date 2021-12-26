import psycopg2 
from tkinter import *
from tkinter import ttk

DB_HOST = "localhost"
DB_NAME = "projekt"
DB_USER = "postgres"
DB_PASS = "postgres"

class JoinTreeview:

    def view_join(window):
            join_win = Toplevel(window)
            join_win.title("JOIN")
            join_win.geometry("500x500")

            #zmena štýlu
            style = ttk.Style()
            style.theme_use("clam")

            #Vytvorenie treeview
            my_join = ttk.Treeview(window)
            my_join.pack()

            #definovanie stlpca
            my_join['columns'] = ("ID", "First name")
                
            #formatovanie stlpca
            my_join.column("#0", width=0, stretch=NO) #Musí tu z nejakeho dôvodu byť takto nastaviť aby ho nebolo vidieť 
            my_join.column("ID", anchor=CENTER, width=50)
            my_join.column("First name", anchor=CENTER, width=120)

            my_join.heading("#0", text="", anchor=CENTER)
            my_join.heading("ID", text="ID", anchor=CENTER)
            my_join.heading("First name", text="First name", anchor=CENTER)
            my_join.pack(pady=20)

            def select_join():
                        
                conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
                cur = conn.cursor()

                cur.execute("SELECT a.first_name, b.address_id FROM public.user a LEFT JOIN user_has_address b ON a.user_id = b.user_id;")
                data = cur.fetchall()

                global count 
                count = 0
                for record in data:
                    my_join.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1]))
                    count += 1

                conn.commit()
                cur.close()
                conn.close()
            
            select_join()