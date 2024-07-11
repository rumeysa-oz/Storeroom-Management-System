from tkinter import *
from tkinter import messagebox
from Userlogin import Login
from Admin_menu import RawMaterials


# MAIN WINDOW
class Visualize(Login,RawMaterials):

    def __init__(self):
        Login.__init__(self)
        self.loginw.mainloop()
        self.loginw.state('withdraw')  # LOGIN WINDOW EXITS
        self.mainw = Toplevel(bg="white")
        width = 1400
        height = 780
        screen_width = self.mainw.winfo_screenwidth()
        screen_height = self.mainw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainw.title("Storeroom Management System")
        self.mainw.resizable(0,0)
        self.mainw.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        self.getdetails()

    # OVERRIDING CLOSE BUTTON && DESTRUCTOR FOR CLASS LOGIN AND MAIN WINDOW
    def __Main_del__(self):
        if messagebox.askyesno("Quit", " Leave Storeroom Management System?") == True:
            self.loginw.quit()
            self.mainw.quit()
            exit(0)
        else:
            pass

    # FETCH DETAILS FROM PRODUCTS, RAW MATERIALS AND PRODUCT TABLE
    def getdetails(self):
        self.cur.execute("CREATE TABLE if not exists products (name varchar (200), date_of_production varchar (250), name_of_customer varchar (500), product_expiration_date varchar (500), storage_code varchar (500), list_of_row_materials_code varchar (500), descriptions varchar (500), PRIMARY KEY(name));")
        self.cur.execute("CREATE TABLE if not exists rowMaterials (name varchar (200), date_of_purchase varchar (250), name_of_suplier varchar (500), storage_expiration_date varchar (500), storage_code varchar (500), descriptions varchar (500), PRIMARY KEY(name));")
        self.cur.execute("select * from products ")
        self.products = self.cur.fetchall()
        l = self.cur.fetchall()
        self.buildmain()


    #  ADD WIDGETS TO TOP OF MAIN WINDOW
    def buildmain(self):

        super(RawMaterials).__init__()
        self.main_menu(8,8)
        self.logout.config(command=self.__Main_del__)
        self.topframe=LabelFrame(self.mainw,width=1400,height=120,bg="#4267b2")
        self.topframe.place(x=0,y=0)
        self.storelable=Label(self.topframe,text="The Storeroom Management System",bg="#4267b2",anchor="center")
        self.storelable.config(font="Roboto 30 bold",fg="snow")
        self.storelable.place(x=360,y=30)
      


if __name__ == '__main__':
    w =  Visualize()
    w.base.commit()
    w.mainw.mainloop()
