from tkinter import *
from sql_data import Sql

class Login:

    def loginScreen(self, window):
        
        sql = Sql()

        window.title("Postgres Database")
        window.geometry("500x250")

        frame = LabelFrame(window, padx=50, borderwidth=0)
        frame.pack(padx=10,pady=10)

        label_mail_1 = Label(frame, text="Enter email:")
        label_mail_2 = Label(frame, text="Enter password:")
        label_mail_1.grid(row=0, column=0)
        label_mail_2.grid(row=1,column=0)

        t1 = Entry(frame, width=10)
        t2 = Entry(frame, width=10)
        t1.grid(row=0, column=1)
        t2.grid(row=1,column=1)

        
        login_button1 = Button(window, text="LOG IN", command=sql.loginSql)
        login_button1.pack()