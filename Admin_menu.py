import cv2
import sqlite3
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Addtional_features import mycombobox,myentry
from tkinter import filedialog
from PIL import Image, ImageTk


class RawMaterials:

    def __init__(self,mainw):
        self.mainw=mainw

    # ADD MAIN MENU TO WINDOW, ALL FRAMES AND ADD IMAGE BUTTONS
    def main_menu(self,a,b):
         self.mainframe = LabelFrame(self.mainw, width=1200, height=145, bg="light blue")
         self.mainframe.place(x=100, y=100)
        
         mi = PhotoImage(file="logout.png")
         mi = mi.subsample(a,b)
         self.logout = Button(self.mainframe, text="Quit", bd=5, font="roboto 11 bold", image=mi, compound=TOP)
         self.logout.image = mi
         self.logout.place(x=1050, y=27)
         
         mi = PhotoImage(file="raw_materials.png")
         mi = mi.subsample(a,b)
         self.rawMaterials = Button(self.mainframe, text="Raw Materials",bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.addRowMaterials)
         self.rawMaterials.image = mi
         self.rawMaterials.place(x=47, y=27)
         
         mi = PhotoImage(file="product.png")
         mi = mi.subsample(a,b)
         self.products = Button(self.mainframe, text="Products",bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.addProducts)
         self.products.image = mi
         self.products.place(x=347, y=27)
         
         mi = PhotoImage(file="capture_video.png")
         mi = mi.subsample(a,b)
         self.capture_button =Button(self.mainframe, text="Capture", bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.capture_video)
         self.capture_button.image = mi
         self.capture_button.place(x=647, y=27)

         mi = PhotoImage(file="Stock.png")
         mi = mi.subsample(a,b)
         self.stocks = Button(self.mainframe, text="Stock",bd=5, image=mi, font="roboto 11 bold", compound=TOP, command=self.build_stock_table)
         self.stocks.image = mi
         self.stocks.place(x=847, y=27)

        
         self.formframe = Frame(self.mainw, width=500, height=550, bg="#FFFFFF")
         self.formframe.place(x=100, y=315)
         self.formframeinfo = self.formframe.place_info()
         self.tableframe1 = LabelFrame(self.mainw, width=350, height=700)
         self.tableframe1.place(x=1200, y=315, anchor=NE)
         self.tableframe1info = self.tableframe1.place_info()
         self.tableframe = LabelFrame(self.mainw, width=350, height=700)
         self.tableframe.place(x=1300, y=315, anchor=NE)
         self.tableframeinfo=self.tableframe.place_info()
         self.itemframe = Frame(self.mainw, bg="#FFFFFF", width=600, height=300)
         self.itemframe.place(x=420, y=280, anchor=NW)
         self.itemframeinfo=self.itemframe.place_info()
         self.formframe1 = Frame(self.mainw, width=500, height=445, bg="#FFFFFF")
         self.formframe1.place(x=100,y=275)
         self.formframe1info = self.formframe1.place_info()
         self.searchframe = Frame(self.mainw, width=720, height=70, bg="#FFFFFF")
         self.searchframe.place(x=575, y=260)
         self.searchframeinfo = self.searchframe.place_info()
         self.searchbut = Button(self.searchframe, text="Search Name", font="roboto 14", bg="#FFFFFF", bd=5, command=self.search_product)
         self.searchbut.place(x=0, y=20, height=40)
         self.searchvar=StringVar()
         self.searchentry = myentry(self.searchframe, textvariable=self.searchvar, font="roboto 14", width=25, bg="#FFFFFF")
         self.searchentry.place(x=210, y=20, height=40)
         self.cur.execute("select name from products")
         li = self.cur.fetchall()
         a = []
         for i in range(0, len(li)):
             a.append(li[i][0])
         self.searchentry.set_completion_list(a)
         self.resetbut = Button(self.searchframe, text="Reset", font="roboto 14", bd=5, width=8, bg="#FFFFFF", command=self.reset_stock_table)
         self.resetbut.place(x=510, y=18, height=40)
            # create a button for selecting an image
         self.image_button = Button(self.searchframe, text="Select Image", font="roboto 14", bd=5, width=10, bg="#FFFFFF", command=self.select_image)
         self.image_button.place(x=590, y=18, height=40) 
         self.cond=0
         self.build_stock_table()

    # MAIN MENU ENDS

    def capture_video(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, mainframe = self.cap.read()
            cv2.imshow("Storeroom", mainframe)
            if cv2.waitKey(1) == 27:
                break
            self.cap.release()
        cv2.destroyAllWindows()

    # BUILD PRODUCT TABLE AT STOCK
    def build_stock_table(self):
         self.searchframe.place_forget()
         self.tableframe.place(self.tableframeinfo)
         self.formframe.place(self.formframeinfo)
         self.tableframe1.place_forget()
         self.formframe1.place_forget()
         self.itemframe.place_forget()
         if(self.cond==1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
    
         scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
         scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
         self.tree = ttk.Treeview(self.tableframe, columns=("Name", "Date of Production", "Name of Customer", "Product expiration date",
         'Storage Code', 'Description', 'List of Raw Material Code'), selectmode="browse", height=18,yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=100)
         self.tree.column('#2', stretch=NO, minwidth=0, width=150)
         self.tree.column('#3', stretch=NO, minwidth=0, width=150)
         self.tree.column('#4', stretch=NO, minwidth=0, width=150)
         self.tree.column('#5', stretch=NO, minwidth=0, width=100)
         self.tree.column('#6', stretch=NO, minwidth=0, width=150)
         self.tree.column('#7', stretch=NO, minwidth=0, width=100)
         self.tree.heading('Name', text="Name", anchor=W)
         self.tree.heading('Date of Production', text="Date of Production", anchor=W)
         self.tree.heading('Name of Customer', text="Name of Customer", anchor=W)
         self.tree.heading('Product expiration date', text="Product expiration date", anchor=W)
         self.tree.heading('Storage Code', text="Storage Code", anchor=W)
         self.tree.heading('Description', text="Description", anchor=W)
         self.tree.heading('List of Raw Material Code', text="List of Raw Material Code", anchor=W)
        
         self.tree.grid(row=1, column=0, sticky="W")
         scrollbary.config(command=self.tree.yview)
         scrollbarx.grid(row=2, column=0, sticky="we")
         scrollbarx.config(command=self.tree.xview)
         scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
         self.get_rawMaterials()
         self.get_products() 
         self.cond=1
         self.main_search(1)

    # SEARCH FRAME FOR STOCK TABLE
    def main_search(self, f):
        self.searchvar.set('')
        if (f==1):
            self.searchframe.config(width=720)
            self.searchframe.place(x=575, y=245)
            self.searchbut.config(text="Search Description",command=self.search_product)
            self.searchbut.place(x=0, y=23, height=37)
            self.searchentry.config(textvariable=self.searchvar,width=20)
            self.searchentry.place(x=210, y=25, height=35)
            self.cur.execute("select descriptions from rowMaterials")
            self.cur.execute("select descriptions from products")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.searchentry.set_completion_list(a)
            self.resetbut.config(command=self.reset_stock_table)
            self.resetbut.place(x=460, y=22, height=37)

    # FETCH PRODUCTS FROM PRODUCTS TABLE
    def get_products(self,x=0):
         ans=''
         self.cur.execute("select * from products")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans

    # FETCH RAW MATERIAL FROM RAW MATERIAL TABLE
    def get_rawMaterials(self,x=0):
         ans=''
         self.cur.execute("select * from rowMaterials")
         productlist = self.cur.fetchall()
         for i in productlist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans

    def search_product(self):
        if (self.searchvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from products")
        self.cur.execute("select * from rowMaterials")
        li=self.cur.fetchall()
        for i in li:
            if(i[2]==self.searchvar.get()):
                self.tree.insert('', 'end', values=(i))

    def reset_stock_table(self):
        self.searchvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.get_products()

    # FUNCTION FOR RAW MATERIALS BUTTON
    def addRowMaterials(self):
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemframe.place(self.itemframeinfo)
        self.newitemname = StringVar()
        self.newitemdate = StringVar()
        self.newitemsup = StringVar()
        self.newitemexp = StringVar()
        self.newitemstorage  = StringVar()
        self.newitemdesc = StringVar()
        l=["Name","Date of Purchase","Name of Supplier","Storage Expiration Date","Storage code","Description"]
        for i in range(0,len(l)):
            Label(self.itemframe,text=l[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i, column=0, pady=15, sticky="w")
        Entry(self.itemframe,width=40,textvariable=self.newitemname,font="roboto 11",bg="#ffffff").grid(row=0, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemdate,font="roboto 11",bg="#ffffff").grid(row=1, column=1, pady=15, padx=10, ipady=3)
        sup=myentry(self.itemframe,width=40,textvariable=self.newitemsup,font="roboto 11",bg="#ffffff")
        sup.grid(row=2, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemexp,font="roboto 11",bg="#ffffff").grid(row=3, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemstorage,font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemframe,width=40,textvariable=self.newitemdesc,font="roboto 11",bg="#ffffff").grid(row=5, column=1, pady=10, padx=8, ipady=3)
        self.cur.execute("select * from rowMaterials")
        li=self.cur.fetchall()
        a=[]
        self.desc_name=[]
        for i in range(0,len(li)):
            if(a.count(li[i][0])==0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
        sup.set_completion_list(a)
        Button(self.itemframe, text="Add item", height=3, bd=6, command=self.insert_rowMaterials, bg="#FFFFFF").grid(row=7, column=1, pady=10, padx=12, sticky="w", ipadx=10)
        Button(self.itemframe, text="Back", height=3, width=8, bd=6,command=self.build_stock_table, bg="#FFFFFF").grid(row=7, column=1, pady=10, padx=16, sticky="e", ipadx=10)


# FUNCTION FOR PRODUCTS BUTTON
    def addProducts(self):
        self.formframe1.place_forget()
        self.searchframe.place_forget()
        self.tableframe.place_forget()
        self.tableframe1.place_forget()
        self.formframe.place_forget()
        self.itemframe.place(self.itemframeinfo)
        self.newitemname = StringVar()
        self.newitemdate = StringVar()
        self.newitemcus = StringVar()
        self.newitemexp = StringVar()
        self.newitemstorage  = StringVar()
        self.newitemdesc = StringVar()
        self.newitemlist = StringVar()
        l1=["Name","Date of Production","Name of Customer","Product Expiration Date","Storage Code","Description","List of Raw Material Code"]
        for i in range(0,len(l1)):
            Label(self.itemframe,text=l1[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i, column=0, pady=5, sticky="w")
        Entry(self.itemframe,width=40,textvariable=self.newitemname,font="roboto 11",bg="#ffffff").grid(row=0, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemdate,font="roboto 11",bg="#ffffff").grid(row=1, column=1, pady=10, padx=10, ipady=3)
        cus=myentry(self.itemframe,width=40,textvariable=self.newitemcus,font="roboto 11",bg="#ffffff")
        cus.grid(row=2, column=1, pady=10, padx=10, ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemexp,font="roboto 11",bg="#ffffff").grid(row=3, column=1, pady=10, padx=10,ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemstorage,font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=10, padx=10,ipady=3)
        Entry(self.itemframe,width=40,textvariable=self.newitemdesc,font="roboto 11",bg="#ffffff").grid(row=5, column=1, pady=10, padx=8, ipady=3)
        Entry(self.itemframe, width=40, textvariable=self.newitemlist,font="roboto 11",bg="#ffffff").grid(row=6, column=1, pady=10, padx=10,ipady=3)
        self.cur.execute("select * from products")
        li=self.cur.fetchall()
        a=[]
        self.desc_name=[]
        for i in range(0,len(li)):
            if(a.count(li[i][0])==0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
        cus.set_completion_list(a)
        Button(self.itemframe, text="Add item", height=3, bd=6, command=self.insert_product, bg="#FFFFFF").grid(row=7,column=1,pady=10,padx=12,sticky="w",ipadx=10)
        Button(self.itemframe, text="Back", height=3, width=8, bd=6, command=self.build_stock_table, bg="#FFFFFF").grid(row=7, column=1, pady=10, padx=16,sticky="e",ipadx=10)

    #  ADD'S PRODUCT
    def insert_product(self):
        self.cur.execute("insert into products values(?,?,?,?,?,?,?)",(
        self.newitemname.get(),self.newitemdate.get(),self.newitemcus.get(),self.newitemexp.get(),self.newitemstorage.get(),self.newitemdesc.get(),self.newitemlist.get()))
        self.newitemname.set('')
        self.newitemdate.set('')
        self.newitemcus.set('')
        self.newitemdesc.set('')
        self.newitemexp.set('')
        self.newitemstorage.set('')
        self.newitemlist.set('')
        messagebox.showinfo('Success','Product added successfully')
        self.base.commit()


        #  ADD'S ROW MATERIALS
    def insert_rowMaterials(self):
        self.cur.execute("insert into rowMaterials values(?,?,?,?,?,?)",(
        self.newitemname.get(),self.newitemdate.get(), self.newitemsup.get(), self.newitemexp.get(),self.newitemstorage.get(),self.newitemdesc.get()))
        self.newitemname.set('')
        self.newitemdate.set('')
        self.newitemsup.set('')
        self.newitemdesc.set('')
        self.newitemexp.set('')
        self.newitemstorage.set('')
        messagebox.showinfo('Success','Raw Material added successfully')
        self.base.commit()



    def select_image(self):
        # open a file dialog to select an image
        filepath = filedialog.askopenfilename()
        # open the selected image using PIL
        img = Image.open(filepath)
        # convert the image to a PhotoImage object
        img = ImageTk.PhotoImage(img)
        # create a label to display the image
        label = tk.Label(self.root, image=img)
        label.image = img
        label.pack()