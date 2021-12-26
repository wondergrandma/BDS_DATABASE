from tkinter import *
from tree_view import TreeView
from login import Login


window = Tk()
tree_w = TreeView()
login = Login()

tree_w.viewDatabase(window)

#login.loginScreen(window)

window.mainloop()