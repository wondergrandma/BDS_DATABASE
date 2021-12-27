from tkinter import *
from tree_view import TreeView
from login import Login

window = Tk()
tree_w = TreeView()
#login = Login()

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

    email_entry = Entry(frame, width=10)
    pwd_entry = Entry(frame, width=10)
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
            print("SUCCESS")
        else:
            print("NO SUCCESS")

    login_button1 = Button(window, text="LOG IN", command = comparePasswords)
    login_button1.pack()

#tree_w.viewDatabase(window)

#login.loginScreen(window)


loginScreen()
window.mainloop()

#oliverbielik@gmail.com
#ahoj