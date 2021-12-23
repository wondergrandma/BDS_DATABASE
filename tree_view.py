from typing import TYPE_CHECKING
import psycopg2 
from tkinter import *
from tkinter import ttk

#Premené pre pripojenie aplikácie k PG admin
DB_HOST = "localhost"
DB_NAME = "projekt"
DB_USER = "postgres"
DB_PASS = "postgres"

class TreeView:

    def viewDatabase(self, window):
        #Vytvorenie okna
        window.title("Postgres Databse")
        window.iconbitmap()
        window.geometry("1030x550")

        #zmena štýlu
        style = ttk.Style()
        style.theme_use("clam")

        #Vytvorenie treeview
        my_tree = ttk.Treeview(window)
        my_tree.pack()

        #definovanie stlpca
        my_tree['columns'] = ("ID", "First name", "Second name" ,"Email" ,"Password")
        
        #formatovanie stlpca
        my_tree.column("#0", width=0, stretch=NO) #Musí tu z nejakeho dôvodu byť takto nastaviť aby ho nebolo vidieť 
        my_tree.column("ID", anchor=CENTER, width=50)
        my_tree.column("First name", anchor=CENTER, width=120)
        my_tree.column("Second name", anchor=CENTER, width=120)
        my_tree.column("Email", anchor=CENTER, width=250)
        my_tree.column("Password", anchor=CENTER, width=490)

        #vytvorenie hlaviciek
        my_tree.heading("#0", text="", anchor=CENTER)
        my_tree.heading("ID", text="ID", anchor=CENTER)
        my_tree.heading("First name", text="First name", anchor=CENTER)
        my_tree.heading("Second name", text="Second name", anchor=CENTER)
        my_tree.heading("Email", text="Email", anchor=CENTER)
        my_tree.heading("Password", text="Password", anchor=CENTER)

        #vypísanie dát z PG admin
        def readData():
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()
                
            cur.execute("SELECT user_id, first_name, second_name, mail, pwd FROM \"user\"")
            conn.commit()
            data = cur.fetchall()
            cur.close()

            global count 
            count = 0
            for record in data:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4]))
                count += 1
            
            conn.close()

        my_tree.pack(pady=20)

        frame = Frame(window)
        frame.pack(pady=20)

        #Labels
        id_label = Label(frame, text="ID")
        id_label.grid(row=0, column=0)
        fname_label = Label(frame, text="Frist name")
        fname_label.grid(row=0, column=1)
        sname_label = Label(frame, text="Second name")
        sname_label.grid(row=0, column=2)
        email_label = Label(frame, text="Email")
        email_label.grid(row=0, column=3)
        pwd_label = Label(frame, text="Password")
        pwd_label.grid(row=0, column=4)

        #Entry box
        id_box = Entry(frame)
        id_box.grid(row=1, column=0)
        fname_box = Entry(frame)
        fname_box.grid(row=1, column=1)
        sname_box = Entry(frame)
        sname_box.grid(row=1, column=2)
        email_box = Entry(frame)
        email_box.grid(row=1,column=3)
        pwd_box = Entry(frame)
        pwd_box.grid(row=1, column=4)

        #funkcia na pridanie záznamu
        def add_record():
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()

            global count
            my_tree.insert(parent='', index='end', iid=count, text="", values=(id_box.get(), fname_box.get(), sname_box.get(), email_box.get(), pwd_box.get()))
            count += 1

            cur.execute("INSERT INTO \"user\" (user_id, bank_branch_id, first_name, second_name, mail, pwd) VALUES (%s,%s,%s,%s,%s,%s);", (id_box.get(), 5, fname_box.get(), sname_box.get(), email_box.get(), pwd_box.get()))

            conn.commit()
            cur.close()
            
            #Vyčistenie boxov po tom ako sa spusti funkcia
            id_box.delete(0, END)
            fname_box.delete(0, END)
            sname_box.delete(0, END)
            email_box.delete(0, END)
            pwd_box.delete(0, END)
        
        def delete_record():
            x = my_tree.selection()[0]
            my_tree.delete(x)

            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()
                
            cur.execute("DELETE CASCADE FROM \"user\" WHERE user_id = " + id_box.get())

            conn.commit()
            cur.close()
        
        def update_record():
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()

            selected = my_tree.focus()
            my_tree.item(selected, text="", values=(id_box.get(), fname_box.get(), sname_box.get(), email_box.get(), pwd_box.get()))
            cur.execute("UPDATE \"user\" SET first_name = ':fname', second_name = ':sname', mail = ':email' WHERE user_id = :id;",
            {'fname': fname_box.get(), 
             'sname': sname_box.get(), 
             'mail': email_box.get(), 
             'id': id_box.get()})


            conn.commit()
            cur.close()

            #Vyčistenie boxov po tom ako sa spusti funkcia
            id_box.delete(0, END)
            fname_box.delete(0, END)
            sname_box.delete(0, END)
            email_box.delete(0, END)
            pwd_box.delete(0, END)


        #Funkcia pre vloženie udajov do poľa po kliknutí myšou
        def clicker(e):
            #Vyčistenie boxov
            id_box.delete(0, END)
            fname_box.delete(0, END)
            sname_box.delete(0, END)
            email_box.delete(0, END)
            pwd_box.delete(0, END)

            selected = my_tree.focus()
            values = my_tree.item(selected, 'values') 

            id_box.insert(0, values[0])
            fname_box.insert(0, values[1])
            sname_box.insert(0, values[2])
            email_box.insert(0, values[3])
            pwd_box.insert(0, values[4])


        my_tree.bind("<ButtonRelease-1>", clicker)


        #Buttons
        add = Button(window, text="Add",command=add_record)
        add.pack(pady=20)

        remove = Button(window, text="Remove", command=delete_record)
        remove.pack(pady=20)

        update = Button(window, text="Update", command=update_record)
        update.pack(pady=20)

        


        readData()