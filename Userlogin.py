

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# LOGIN CLASS
class Login:

    def __init__(self):
        self.loginw=Tk()
        self.loginw.title("Storeroom Management System")
        width = 500
        height = 600
        screen_width = self.loginw.winfo_screenwidth()
        screen_height = self.loginw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.loginw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg="white")
        self.logintable()
        self.loginframe=LabelFrame(self.loginw,bg="#f7f9fc",height=400,width=380)
        self.loginw.bind('<Return>',self.success)
        self.loginframe.place(x=70,y=95)
        self.toplabel = Label(self.loginframe, fg="white", bg="#4267b2", anchor="center", text="Storeroom \n Management \n System", font="Roboto 40 bold")
        self.toplabel.place(x=5,y=25)
        self.signin = Button(self.loginframe,width=20, text="Click for System",bg="lightblue2",fg="dimgray",command=self.success, font="Roboto 14")
        self.signin.place(x=65,y=290)

    def __login_del__(self):
        if messagebox.askyesno("Quit", " Leave storeroom?") == True:
            self.loginw.destroy()
            exit(0)                  

    # LOGIN SQLite Database
    def logintable(self):
        self.base = sqlite3.connect("sqlite.db")
        self.cur = self.base.cursor()

    # LOGIN SUCCESS
    def success(self):
        self.loginw.quit()



