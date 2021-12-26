import logging
from tkinter import *
import bcrypt
import hashlib

class Login:

    """mail = ""
    password = ""
    
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password
        self.hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())"""

    def loginScreen(self, window):
        
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

        def hashPwd():
            get_pwd = str(t2.get())
            hash_pwd = str(get_pwd.hashlib.sha256(bytes).hexdigest())
            return hash_pwd

            
        
        login_button1 = Button(window, text="LOG IN", command = hashPwd)
        login_button1.pack()