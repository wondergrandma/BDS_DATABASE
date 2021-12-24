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
        my_tree.pack(pady=20)

        #Vytvorenie okna na simuláciu injection
        def dummy_table():
            global dummy_box

            dummy_win = Toplevel(window)
            dummy_win.title("Dummy table")
            dummy_win.geometry("200x200")

            dummy_frame = LabelFrame(dummy_win, text="")
            dummy_frame.pack(padx=10, pady=10)

            dummy_box = Entry(dummy_frame)
            dummy_box.pack(padx=20, pady=20)

            dummy_button = Button(dummy_win, text="Injection", command=sql_injection)
            dummy_button.pack(padx=20, pady=20)

        #Napojenie na databázu bez preapered statementu
        def sql_injection():
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()

            cur.execute(dummy_box.get())
            #cur.fetchall()

            conn.commit()
            cur.close()
            print("YOU SUCCESFULLY DROPED TABLE WITH SQL INJECTION "+ "\""+dummy_box.get()+"\"")

        #Search podla priezviska
        def search_lname():
            global count 
            count = 0

            find_data = search_box.get()
            search_win.destroy()

            for data in my_tree.get_children():
                my_tree.delete(data)
            
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()
                
            cur.execute("SELECT user_id, first_name, second_name, mail, pwd FROM \"user\" WHERE second_name =  " + "'"+find_data+"'")
            data = cur.fetchall()

            for record in data:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]))
                count += 1

            conn.commit()
            cur.close()

        #Vytvorenie search okna
        def search_records():
            global search_box, search_win

            search_win = Toplevel(window)
            search_win.title("Search")
            search_win.geometry("200x200")

            frame_win = LabelFrame(search_win, text="")
            frame_win.pack(padx = 10, pady = 10)

            search_box= Entry(frame_win)
            search_box.pack(padx = 20, pady = 20)

            search_button = Button(search_win, text="Search", command = search_lname)
            search_button.pack(padx = 20, pady = 20)

        #vypísanie dát z PG admin
        def readData():
            #Funkcia na zmazanie predošlých dát dalej je implementovaná v tlačítku
            for data in my_tree.get_children():
                my_tree.delete(data)

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


        def join_func():
            global count 
            count = 0

            search_win.destroy()

            for data in my_tree.get_children():
                my_tree.delete(data)
            
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()
                
            cur.execute("SELECT a.first_name, b.address_id FROM public.user a LEFT JOIN user_has_address b ON a.user_id = b.user_id")
            data = cur.fetchall()

            for record in data:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]))
                count += 1

            conn.commit()
            cur.close()

        #my_tree.pack(pady=20)

        #Vytvorenie menu
        my_options = Menu(window)
        window.config(menu = my_options)

        search_menu = Menu(my_options, tearoff=0)
        my_options.add_cascade(label="Option", menu = search_menu)

        search_menu.add_command(label="Search", command = search_records)
        search_menu.add_command(label="Reset", command = readData)
        search_menu.add_command(label="JOIN", command = join_func)
        search_menu.add_command(label="Dummy", command = dummy_table)
        search_menu.add_command(label="Exit", command = window.quit)

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

            cur.execute("DELETE FROM user_has_role WHERE user_id = " + id_box.get())
            cur.execute("DELETE FROM user_has_address WHERE user_id = " + id_box.get())
            cur.execute("DELETE FROM card WHERE user_id = " + id_box.get())    
            cur.execute("DELETE FROM \"user\" WHERE user_id = " + id_box.get())
                
            conn.commit()
            cur.close()
           
        def update_record():
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            cur = conn.cursor()

            selected = my_tree.focus()
            my_tree.item(selected, text="", values=(id_box.get(), fname_box.get(), sname_box.get(), email_box.get(), pwd_box.get()))
            cur.execute("UPDATE \"user\" SET first_name = %s, second_name = %s, mail = %s WHERE user_id = %s;", (fname_box.get(), sname_box.get(), email_box.get(), id_box.get(),))
            
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