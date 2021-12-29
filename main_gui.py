from tkinter import *
from tkinter import messagebox
from tree_view import TreeView
import logging
from login import Login

window = Tk()
tree_w = TreeView()

#Logging
logging.basicConfig(
level=logging.INFO,
format= "{asctime} {levelname:<8} {message}",
style='{',
filename='activity_log.log',
filemode='a'
)

def warningMsg():
    messagebox.showinfo("WARNING", "Username or password is not valid")

def loginScreen():
    global email_entry, pwd_entry
    window.title("Postgres Database")
    window.geometry("500x250")

    frame = LabelFrame(window, padx=50, borderwidth=0)
    frame.pack(padx=10,pady=10)

    label_mail_1 = Label(frame, text="Enter email:")
    label_mail_2 = Label(frame, text="Enter password:")
    label_mail_1.grid(row=0, column=0)
    label_mail_2.grid(row=1,column=0)

    email_entry = Entry(frame, width=20)
    pwd_entry = Entry(frame, width=20, show = '*')
    email_entry.grid(row=0, column=1)
    pwd_entry.grid(row=1,column=1)

    def comparePasswords():
        global email
        email = email_entry.get()
        global password
        password = pwd_entry.get()
        global lg
        lg = Login(email, password)

        if (lg.comparePasswords() == True):
            logging.info('Showing database data to user: ' +email)
            logging.info('APPLICATION SUCCESSFULY STARTED -> user: '+email)
            tree_w.viewDatabase(window)
        else:
            logging.info('WRONG -> user: '+email)
            warningMsg()

    login_button1 = Button(window, text="LOG IN", command = comparePasswords)
    login_button1.pack()

loginScreen()
window.mainloop()