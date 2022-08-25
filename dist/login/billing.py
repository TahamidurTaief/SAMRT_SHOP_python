from concurrent.futures import process
from doctest import master
from email import message
from email.mime import image
import tempfile
from tkinter import *
from turtle import color, left, onclick
from typing import List
from unicodedata import name
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import time
import os
import create_db 

from product import productClass
from settings import settingClass


from requests import delete





class billinngClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1300x770+0+0')
        self.root.config(bg=f"#10213b")
        self.root.iconbitmap('images/icon.ico')
        self.root.title("Welcome to Smart Shop | Product of exeyezone")

        self.var_search = StringVar()

        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_mrp = StringVar()
        self.var_dp = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        self.cart_list = []
        self.chk_print=0
        self.var_stock = StringVar()
        self.var_cname = StringVar()
        self.var_contact = StringVar()
        self.var_paid_unpaid = StringVar()
        self.var_paid = StringVar()
        self.var_customer_id = StringVar()
        self.var_due = StringVar()

        self.var_color_code = StringVar()


        self.var_txt=StringVar()
        self.var_oparetor=''




    # ==============  title of main frame  ==============
        con = sqlite3.connect(database =r"yms.db")
        cur = con.cursor()
        try:
            
            self.root.icon_title=PhotoImage(file="images/title_bar.png")
            title=Label(self.root,image=self.root.icon_title).place(x=0, y=0, relwidth=1)

            cur.execute("SELECT name FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]

            title_lbl = Label(self.root, text=f"{name}", font=("Montserrat", 19, "bold"), relief=FLAT, bg="#1D2142", fg= "#ffac48")
            title_lbl.place(x=270, y=12)

            con.commit()
            cur.close()

        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {es}")


    #  ============== logout button  ==============
        self.root.logout_btn = PhotoImage(file="images/singout.png")
        logout_btn=Button(self.root,command=self.logout, image=self.root.logout_btn, bg="#1D2142", bd=0, cursor="hand2", activebackground="#1D2142")
        logout_btn.place(x=1100, y=10)

    # exeyezone logo
        self.root.exeyezone_logo = PhotoImage(file="images/exeyezoneLogo.png")
        exeyezone_logo = Label(self.root, image=self.root.exeyezone_logo, bg="#1D2142", bd=2)
        exeyezone_logo.place(x=950, y=10)



    # ==============  Clock Label  ==============

        self.clock_label=Label(self.root, text=f"Welcome to SMART SHOP \t\t\t DD:MM:YY \t\t\t SS:MM:HH", font=("Montserrat", 15), bg="#245e5b", fg="white")
        self.clock_label.place(x=0, y=55, relwidth=1)


# ======================      Product Frame     ===============================================

        productFrame = Frame(self.root, bg="#1F3043")
        productFrame.place(x=15, y=100, width=370, height=615)

        # ===========================    Products Frame Heading    ============================

        productFrame_heading = Label(productFrame, text="ALL PRODUCTS", bg="#245E5B", relief=FLAT, fg="white", font=("Montserrat", 15))
        productFrame_heading.place(x=1, y=1, relwidth=1)

# ===========================    search Frame   ===========================
        search_frame=LabelFrame(productFrame, text="Search Products", font=("goudy old style",12, "bold"), bg="#150739", fg="white", bd=2)
        search_frame.place(x=8, y=40, width=355, height=100)

        # ====================== Entry box and search button in Search frame =======================
        Search_title= Label(search_frame, text="Search Product | By Name",  font=("goudy old style",12), bg="#150739", fg="white")
        Search_title.place(x=5, y=5)

        #name_label ==============
        Search_label= Label(search_frame, text="Product Name", font=("goudy old style",12), bg="#150739", fg="white")
        Search_label.place(x=5, y=45)

        # Entry ===========
        search_frame_entry= Entry(search_frame, textvariable=self.var_search, font=("goudy old style",12), bg="#9ecffc", fg="black")
        search_frame_entry.place(x=120, y=45, width=150, height=25)

        #Button ===========
        self.search_btn=PhotoImage(file="images/search_icon_btn.png")
        search_btn=Button(search_frame, image=self.search_btn,command=self.search, bg="#150739", relief=FLAT, activebackground="#150739", bd=0)
        search_btn.place(x=300, y=40)

        self.show_all_btn=PhotoImage(file="images/show_all_icon.png")
        search_btn=Button(search_frame, image=self.show_all_btn, bg="#150739", relief=FLAT, activebackground="#150739", bd=0)
        search_btn.place(x=300, y=2)



    # ===================     Product tree   ===============================
        product_list_Frame = Frame(productFrame, bd=5, relief=FLAT, bg="#9ECFFC" )
        product_list_Frame.place(x=5, y=175, width=355, height=400)

        scrolly = Scrollbar(product_list_Frame, orient=VERTICAL)
        scrollx = Scrollbar(product_list_Frame, orient=HORIZONTAL)

        self.productTable= ttk.Treeview(product_list_Frame, columns=("pid", "name", "mrp","dp", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)
        scrolly.config(command=self.productTable.yview)
        scrollx.config(command=self.productTable.xview)

        self.productTable.heading('pid', text="PID")
        self.productTable.heading('name', text="Name")
        self.productTable.heading('mrp', text="MRP")
        self.productTable.heading('dp', text="DP")
        self.productTable.heading('qty', text="QTY")
        self.productTable.heading('status', text="Status")

        self.productTable["show"]="headings"

        self.productTable.column('pid', width=70)
        self.productTable.column('name', width=90)
        self.productTable.column('mrp', width=50)
        self.productTable.column('dp', width=50)
        self.productTable.column('qty', width=40)
        self.productTable.column('status', width=60)

        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)

        note_lbl = Label(productFrame, text="Note:  Enter 0 QTY to remove the product from Cart", font=("Montserrat", 10), bg="#1F3043", fg= "white")
        note_lbl.place(x=10, y=585)







# ==================================     customer Details Frame     ====================================

        customerFrame = Frame(self.root, relief=FLAT, bd=2, bg="#1F3043")
        customerFrame.place(x=395, y=100, width=450, height=135)

        customerFrame_heading = Label(customerFrame, text="CUSTOMER DETAILS", bg="#245E5B", relief=FLAT, fg="white", font=("Montserrat", 15))
        customerFrame_heading.place(x=0, y=0, relwidth=1)

        name_lbl = Label(customerFrame, text="Name", font=("Montserrat", 11), bg="#1F3043", fg="white")
        name_lbl.place(x=10, y=50)

        name_entry = Entry(customerFrame,textvariable=self.var_cname, font=("Montserrat", 12), fg="#1F3043", bg="#9ECFFC")
        name_entry.place(x=70, y=50, width=130, height=25)

        contact_lbl = Label(customerFrame, text="Contact", font=("Montserrat", 11), bg="#1F3043", fg="white")
        contact_lbl.place(x=220, y=50)

        contact_entry = Entry(customerFrame,textvariable=self.var_contact, font=("Montserrat", 12), fg="#1F3043", bg="#9ECFFC")
        contact_entry.place(x=300, y=50, width=130, height=25)

        cmd_search = ttk.Combobox(customerFrame,textvariable=self.var_paid_unpaid , values=("PAID", "UNPAID"), state='readonly', justify=CENTER, font=("Montserrat", 10))
        cmd_search.place(x=10, y=90, width=120, height=25)
        cmd_search.current(0)

        paid_lbl = Label(customerFrame, text="PAID", font=("Montserrat", 11), bg="#1F3043", fg="white")
        paid_lbl.place(x=150, y=90)

        paid_entry = Entry(customerFrame, textvariable=self.var_paid, font=("Montserrat", 12), fg="#1F3043", bg="#9ECFFC")
        paid_entry.place(x=200, y=90, width=130, height=25)

        self.add_btn = ImageTk.PhotoImage(file="images/add_btn.png")
        add_btn = Button(customerFrame, image=self.add_btn, relief=FLAT, bd=0, command=self.insert_customer_data , bg="#1F3043", activebackground="#1F3043")
        add_btn.place(x=340, y=85)





#================================       CALC and cart frame     ====================================
        ccFrame = Frame(self.root, relief=FLAT, bd=2, bg="#1F3043")
        ccFrame.place(x=395, y=250, width=450, height=330)

        cal_frame = Frame(ccFrame, relief=RIDGE, bd=2, bg="#191B28")
        cal_frame.place(x=10, y=10, width=210, height=310)



        #===============================    Calclutor   ================================

        #  Entry ========================== 


        
    


        cal_entry = Entry(cal_frame,textvariable=self.var_txt , relief=FLAT,justify=RIGHT, font=("Montserrat", 12, "bold"), fg="#1F3043", bg="#9ECFFC", bd=2)
        cal_entry.place(x=8, y=10, width=190, height=30)

        
        #button of Calclutor
        self.btn_7=PhotoImage(file="images/calclutor/7_btn.png")
        self.btn_8=PhotoImage(file="images/calclutor/8_btn.png")
        self.btn_9=PhotoImage(file="images/calclutor/9_btn.png")
        self.btn_6=PhotoImage(file="images/calclutor/6_btn.png")
        self.btn_5=PhotoImage(file="images/calclutor/5_btn.png")
        self.btn_4=PhotoImage(file="images/calclutor/4_btn.png")
        self.btn_3=PhotoImage(file="images/calclutor/3_btn.png")
        self.btn_2=PhotoImage(file="images/calclutor/2_btn.png")
        self.btn_1=PhotoImage(file="images/calclutor/1_btn.png")
        self.btn_0=PhotoImage(file="images/calclutor/0_btn.png")
        self.btn_div=PhotoImage(file="images/calclutor/div_btn.png")
        self.btn_mul=PhotoImage(file="images/calclutor/mul_btn.png")
        self.btn_min=PhotoImage(file="images/calclutor/minus_btn.png")
        self.btn_clear=PhotoImage(file="images/calclutor/c_btn.png")
        self.btn_equal=PhotoImage(file="images/calclutor/equal_btn.png")
        self.btn_plus=PhotoImage(file="images/calclutor/plus_btn.png")




    #Row1
        btn_7=Button(cal_frame, image=self.btn_7 , cursor="hand2", command=lambda:self.get_input(7), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_7.place(x=1, y=52)
        btn_8=Button(cal_frame, image=self.btn_8, cursor="hand2", command=lambda:self.get_input(8), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_8.place(x=50, y=52)
        btn_9=Button(cal_frame, image=self.btn_9, cursor="hand2", command=lambda:self.get_input(9), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_9.place(x=100, y=52)
        btn_div=Button(cal_frame, image=self.btn_div, cursor="hand2", command=lambda:self.get_input("/"), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_div.place(x=153, y=52)

    #Row 2
        btn_4=Button(cal_frame, image=self.btn_4, cursor="hand2", command=lambda:self.get_input(4), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_4.place(x=1, y=112)
        btn_5=Button(cal_frame, image=self.btn_5, cursor="hand2", command=lambda:self.get_input(5), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_5.place(x=50, y=112)
        btn_6=Button(cal_frame, image=self.btn_6, cursor="hand2", command=lambda:self.get_input(6), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_6.place(x=100, y=112)
        btn_mul=Button(cal_frame, image=self.btn_mul, cursor="hand2", command=lambda:self.get_input("*"), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_mul.place(x=153, y=112)

    #Row 3
        btn_1=Button(cal_frame, image=self.btn_1, cursor="hand2", command=lambda:self.get_input(1), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_1.place(x=1, y=172)
        btn_2=Button(cal_frame, image=self.btn_2, cursor="hand2", command=lambda:self.get_input(2), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_2.place(x=50, y=172)
        btn_3=Button(cal_frame, image=self.btn_3, cursor="hand2", command=lambda:self.get_input(3), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_3.place(x=100, y=172)
        btn_min=Button(cal_frame, image=self.btn_min, cursor="hand2", command=lambda:self.get_input("-"), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_min.place(x=153, y=172)
    
    #Row 4
        btn_0=Button(cal_frame, image=self.btn_0, cursor="hand2", command=lambda:self.get_input(0), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_0.place(x=1, y=232)
        btn_clear=Button(cal_frame, image=self.btn_clear, cursor="hand2", command=self.clear_cal, bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_clear.place(x=50, y=232)
        btn_plus=Button(cal_frame, image=self.btn_plus, cursor="hand2", command=lambda:self.get_input("+"), bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_plus.place(x=100, y=232)
        btn_equal=Button(cal_frame, image=self.btn_equal, cursor="hand2", command=self.perform_cal, bg="#191B28", relief=FLAT, activebackground="#191B28", bd=0)
        btn_equal.place(x=153, y=232)
        credit_lbl=Label(cal_frame ,text="Developed by Tahamidur Taief", font=("Montserrat", 9), bg="#191B28", fg="#DEFFFF")
        credit_lbl.place(x=15, y=290)






    # ===================     Cart Frame tree   ===============================


        cartFrame = Frame(ccFrame, bd=5, relief=FLAT, bg="#9ECFFC" )
        cartFrame.place(x=230, y=10, width=210, height=310)

        self.cartFrame_lbl = Label(cartFrame, text="CART\t Total products[0]", font=("Montserrat", 10, "bold"), bg="#191B28", fg="#DEFFFF")
        self.cartFrame_lbl.pack(side=TOP, fill=X, pady=3)

        scrolly = Scrollbar(cartFrame, orient=VERTICAL)
        scrollx = Scrollbar(cartFrame, orient=HORIZONTAL)

        self.cartTable= ttk.Treeview(cartFrame, columns=("pid", "name", "mrp","dp", "qty"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)
        scrolly.config(command=self.cartTable.yview)
        scrollx.config(command=self.cartTable.xview)

        self.cartTable.heading('pid', text="PID")
        self.cartTable.heading('name', text="Name")
        self.cartTable.heading('mrp', text="MRP")
        self.cartTable.heading('dp', text="DP")
        self.cartTable.heading('qty', text="QTY")

        self.cartTable["show"]="headings"

        self.cartTable.column('pid', width=70)
        self.cartTable.column('name', width=90)
        self.cartTable.column('mrp', width=40)
        self.cartTable.column('dp', width=40)
        self.cartTable.column('qty', width=40)

        self.cartTable.pack(fill=BOTH, expand=1)
        self.cartTable.bind("<ButtonRelease-1>", self.get_cart_data)
        






#===================================       Stock Frame      =======================================
        stockFrame = Frame(self.root, relief=FLAT, bd=2, bg="#1F3043")
        stockFrame.place(x=395, y=590, width=450, height=125)

        # Label ===================

        product_name = Label(stockFrame, text="Product Name", font=("Montserrat", 10), bg="#1F3043", fg="white")
        product_name.place(x=5, y=10)

        mrp_qty = Label(stockFrame, text="MRP Per QTY   ", font=("Montserrat", 10), bg="#1F3043", fg="white")
        mrp_qty.place(x=155, y=10)

        qty = Label(stockFrame, text="Quantity", font=("Montserrat", 10), bg="#1F3043", fg="white")
        qty.place(x=310, y=10)


        #   entry=============

        product_name_entry = Entry(stockFrame,textvariable=self.var_pname, font=("Montserrat", 10), fg="#1F3043", bg="#9ECFFC")
        product_name_entry.place(x=5, y=45, width=130, height=25)

        mrp_qty_entry = Entry(stockFrame,textvariable=self.var_mrp, font=("Montserrat", 10), fg="#1F3043", bg="#9ECFFC")
        mrp_qty_entry.place(x=155, y=45, width=130, height=25)

        qty_entry = Entry(stockFrame,textvariable=self.var_qty, font=("Montserrat", 10), fg="#1F3043", bg="#9ECFFC")
        qty_entry.place(x=310, y=45, width=130, height=25)

        self.product_dp = self.var_dp.get()


        #===================        row-3 label and Button      ===================

        self.instock=Label(stockFrame, text="In Stock  ", font=("Montserrat", 14, "bold"), bg="#1F3043", fg="white")
        self.instock.place(x=10, y=85)


        self.clear_btn = PhotoImage(file="images/clear_btn.png")
        clear_btn = Button(stockFrame, image=self.clear_btn,command=self.clear_cart , relief=FLAT, bg="#233233", cursor="hand2", activebackground="#1F3043", bd=0)
        clear_btn.place(x=170, y=80)

        self.update_btn = PhotoImage(file="images/update_btn.png")
        update_btn = Button(stockFrame, image=self.update_btn, relief=FLAT,command=self.add_update_cart , bg="#233233", cursor="hand2", activebackground="#1F3043", bd=0)
        update_btn.place(x=300, y=80)



# ==================================     customer Bill area Frame     ====================================

        customerFrame = Listbox(self.root, relief=FLAT, bd=2, bg="#245E5B")
        customerFrame.place(x=855, y=100, width=420, height=480)

        customerFrame_heading = Label(customerFrame, text="CUSTOMER BILL AREA", bg="#245E5B", fg="white", font=("Montserrat", 14), relief=FLAT)
        customerFrame_heading.pack(side=TOP, expand=1)

        self.customerFrame_txt = Text(customerFrame, bg="#c0f1fb", fg="black", font=("goury old style", 12))
        self.customerFrame_txt.pack(fill=BOTH, expand=1)


        # Theam
        
        self.bill_area_theam1 = PhotoImage(file="images/bill_area_count.png")
        bill_area_theam1 = Label(self.root, image=self.bill_area_theam1, bd=0, bg="#10213B")
        bill_area_theam1.place(x=865, y=590)

        self.bill_area_theam2 = PhotoImage(file="images/bill_area_count.png")
        bill_area_theam2 = Label(self.root, image=self.bill_area_theam2, bd=0, bg="#10213B")
        bill_area_theam2.place(x=1005, y=590)

        self.bill_area_theam3 = PhotoImage(file="images/bill_area_count.png")
        bill_area_theam3 = Label(self.root, image=self.bill_area_theam3, bd=0, bg="#10213B")
        bill_area_theam3.place(x=1140, y=590)


        #   Text label on theam ======================== 
        self.bill_amount_lbl = Label(self.root, text="Bill Ammount\n0", bg="#334B4C", fg= "white", font = ("Montserrat", 10))
        self.bill_amount_lbl.place(x=870, y=600)

        self.discount_lbl = Label(self.root, text="Profit Money\n0", bg="#334B4C", fg= "white", font = ("Montserrat", 10))
        self.discount_lbl.place(x=1010, y=600)

        self.net_pay_lbl = Label(self.root, text="Net Pay \n 0", bg="#334B4C", fg= "white", font = ("Montserrat", 10))
        self.net_pay_lbl.place(x=1160, y=600)


        # Button =============

        self.print_btn = PhotoImage(file="images/print_btn.png")
        print_btn = Button(self.root, image=self.print_btn,command=self.print_bill, bd=0, bg="#10213B", activebackground="#10213B")
        print_btn.place(x=860, y=675)

        self.clear_btn2 = PhotoImage(file="images/clear_btn2.png")
        clear_btn2 = Button(self.root, command=self.clear_all, image=self.clear_btn2, bd=0, bg="#10213B", activebackground="#10213B")
        clear_btn2.place(x=995, y=675)

        self.save_btn = PhotoImage(file="images/save.png")
        save_btn = Button(self.root,command=self.bill_generator, image=self.save_btn, bd=0, bg="#10213B", activebackground="#10213B")
        save_btn.place(x=1130, y=675)




    # ==============  Footer bar  ==============
        con = sqlite3.connect(database =r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, phone_no, address, email, website FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]
                phone_no = row[1]
                address = row[2]
                email = row[3]
                website = row[4]

                footer = footer = Label(self.root, text=f"{name} |  PRODUCT OF exeyezone \n website: www.exeyezone.com      |      email: exeyezoneltd@gmail.com      |      Contact: 01977794509", font=("Montserrat", 9), bg="#245e5b", fg="white")
                footer.pack(side=BOTTOM, fill=X)
            con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)

        self.show()
        self.bill_top()
        self.update_date_time()







# =============================================     Fuction From Here     ====================================

    def get_input(self, num):
        xnum = self.var_txt.get() + str(num)
        self.var_txt.set(xnum)

    def clear_cal(self):
        self.var_txt.set('')
    
    def perform_cal(self):
        result=self.var_txt.get()
        self.var_txt.set(eval(result))

        
    def show(self):
            con = sqlite3.connect(database=r"yms.db")
            cur = con.cursor()
            try:
                cur.execute("SELECT p_id , name, mrp ,dp, qty, status FROM product where status='Active'")
                rows=cur.fetchall()
                self.productTable.delete(*self.productTable.get_children())
                for row in rows:
                    self.productTable.insert('', END, values=row)


            except Exception as ex:
                messagebox.showerror("Error", f"Your error due to {str(ex)}")

    
    def search(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()

        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error", "Search input should be requierd!", parent=self.root)

            else:
                cur.execute("Select p_id , name, mrp ,dp, qty , status from product where name LIKE '%" +self.var_search.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('', END, values=row)
                
                else:
                    messagebox.showerror("Error", "Result not found!!!", parent=self.root)
                con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {(ex)}", parent=self.root)


        

    def get_data(self, env):
        f= self.productTable.focus()
        content = (self.productTable.item(f))
        row = content['values']

        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_mrp.set(row[2])
        self.var_dp.set(row[3])
        self.instock.config(text=(f"In Stock[{str(row[4])}]"))
        self.var_stock.set(row[4])
        self.var_qty.set('1')

        

    def get_cart_data(self, env):

        f= self.cartTable.focus()
        content = self.cartTable.item(f)
        row = content['values']

        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_mrp.set(row[2])
        self.var_dp.set(row[3])
        self.var_qty.set(row[4])
        self.instock.config(text=(f"In Stock[{str(row[5])}]"))
        self.var_stock.set(row[5])
        # self.var_qty.set('1')

    def insert_customer_data(self):
        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            if self.var_cname.get()=="":
                messagebox.showerror("Error", "Employee Id must be required.", parent=self.root)

            else:
                cur.execute("SELECT * FROM customer WHERE cus_name=?", (self.var_cname.get(),))
                row = cur.fetchone()
                cur.execute("INSERT INTO customer (cus_name, customer_bill, payment, paid, p_name, product_qty) VALUES(?,?,?,?,?,?)", (

                        self.var_cname.get(),
                        self.var_mrp.get(),
                        self.var_paid_unpaid.get(),
                        self.var_paid.get(),
                        self.var_pname.get(),
                        self.var_qty.get(),
                    ))
                con.commit()
                messagebox.showinfo("Success", "Customer added Successfully", parent=self.root)
                self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)

        

    
    def add_update_cart(self):
        if self.var_pid.get() == "":
            messagebox.showerror("Error", "Please select product from the list.", parent=self.root)
        elif self.var_qty.get() == "":
            messagebox.showerror("Error", "Quantity must be required", parent=self.root)

        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error", "Insufficient Stock's Products!", parent=self.root)

        else:
            # mrp_qty = float(int(self.var_qty.get())*float(self.var_mrp.get()))
            mrp_cal = self.var_mrp.get()

            cart_data = [self.var_pid.get(), self.var_pname.get(), mrp_cal, self.var_dp.get(), self.var_qty.get(), self.var_stock.get(),]
            


        #================ Update Cart ===================

            present = "no"
            index_ =0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ +=1
 
            
            if present == 'yes':
                op=messagebox.askyesno("Confarm", "Product already present.\n Do you update/ remove product from here.", parent=self.root)
                if op == True:
                    if self.var_qty.get()=='0':
                        self.cart_list.pop(index_)
                        
                    else:
                        # self.cart_list[index_][2]=mrp_qty
                        self.cart_list[index_][4]=self.var_qty.get()

            else:
                self.cart_list.append(cart_data)
                
            self.show_cart()
            self.update_bill()
           

    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {str(ex)}")


    def update_bill(self):
        con = sqlite3.connect(database =r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT discount FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                discount = row[0]

                self.bill_amount = 0
                self.net_pay = 0
                self.discount=0
                self.profit = 0
                # discount = float(discount)
                
                for row in self.cart_list:
                    self.bill_amount = self.bill_amount+(float(row[2]) * int(row[4]))
                    # self.profit = self.bill_amo -unt

                for row in self.cart_list:
                    self.profit = self.bill_amount-int(row[3])

                self.discount=(self.bill_amount*(int(discount)))/100
                self.net_pay = self.bill_amount-self.discount
                # self.payment = self.var_mrp.get()-self.var_paid.get()
                # self.due_payment = float(self.payment)

                self.bill_amount_lbl.config(text=f"Bill Amount\n{str(self.bill_amount)}-BDT")
                self.net_pay_lbl.config(text=f"Net Pay\n{str(self.net_pay)}-BDT")
                self.cartFrame_lbl.config(text=f"CART\t Total products - {str(len(self.cart_list))}")
                self.discount_lbl.config(text=f"Profit Money\n{self.profit}")

        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {es}")


    def bill_generator(self):
        if self.var_cname.get()=="":
            messagebox.showerror("Error", "Customer Details must be required!", parent=self.root)
        
        elif len(self.cart_list)==0:
           messagebox.showerror("Error", "Select a product to the cart!", parent=self.root)

        

        else:
            if self.var_paid_unpaid.get()=='PAID':
                # ==== Bill Top =====
                self.bill_top()
                # ==== BIll Middle ======
                self.bill_middle()
                # ==== Bill Bottom ======
                self.bill_bottom()

            else:
                # ==== Bill Top =====
                self.unpaid_bill_top()
                # ==== BIll Middle ======
                self.unpaid_bill_middle()
                # ==== Bill Bottom ======
                self.unpaid_bill_bottom()

        # ============    Save invoice to bill directory

            fp = open(f'bill/{str(self.invoice)}.txt', 'w')
            fp.write(self.customerFrame_txt.get('1.0', END))
            fp.close()
            messagebox.showinfo("Success", "Your bill generated Successfully and saved to the directory!", parent=self.root)
            self.chk_print=1
            
    
    def bill_top(self):
        con = sqlite3.connect(database =r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, phone_no, address, email, website FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]
                phone_no = row[1]
                address = row[2]
                email = row[3]
                website = row[4]


            self.invoice = int(time.strftime('%H%M%S'))+int(time.strftime("%d%m%y"))
            bill_top_temp=f'''
\t\t{name}
        Phone No. {phone_no} , {address}
    email: {email} , website: {website}\n
{str("="*45)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*45)}
 Product Name\t\t\tQTY\tmrp
{str("="*45)}
        '''
            self.customerFrame_txt.delete('1.0',END)
            self.customerFrame_txt.insert('1.0',bill_top_temp)

        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {str(es)}")


    def bill_bottom(self):
        # self.sample_img_lbl = PhotoImage(file="images/clear_btn.png")
        # sample_img_lbl=Label(self.customerFrame_txt, image=self.sample_img_lbl)
        # sample_img_lbl.place(x=300, y=200)
        bill_bottom_temp=f'''
{str("="*45)}
 Bill Amount\t\t\t\tBDT.{self.bill_amount}
 Discount\t\t\t\tBDT.{self.discount}
 Net Pay\t\t\t\tBDT.{self.net_pay}
{str("="*45)}\n
PAID FULL MONEY
        '''
        self.customerFrame_txt.insert(END,bill_bottom_temp)


          
    def bill_middle(self):
        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            for row in self.cart_list:
            # pid,name,mrp, dp,qty,stock
                p_id = row[0]
                name= row[1]
                qty=int(row[5])-int(row[4])
                # qty=int(row[4])-int(row[3])

                if int(row[4])==int(row[5]):
                    status = 'Inactive'

                if int(row[4])!=int(row[5]):
                    status = 'Active'

                mrp=float(row[2])*int(row[4])
                mrp=str(mrp)
                self.customerFrame_txt.insert(END,"\n "+name+"\t\t\t"+row[4]+"\tBDT."+mrp)


        #   =-=============  update quantity in product table   ======================
                cur.execute("Update product set qty=?, status=? where p_id=?",(
                    qty,
                    status,
                    p_id,
                ))

                con.commit()
            con.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)

# unpaid invoice


    def unpaid_bill_top(self):
        con = sqlite3.connect(database =r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, phone_no, address, email, website FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]
                phone_no = row[1]
                address = row[2]
                email = row[3]
                website = row[4]


            self.invoice = int(time.strftime('%H%M%S'))+int(time.strftime("%d%m%y"))
            bill_top_temp=f'''
\t\t{name}
        Phone No. {phone_no} , {address}
    email: {email} , website: {website}\n
{str("="*45)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*45)}
 Product Name\t\t\tQTY\tmrp
{str("="*45)}
        '''
            self.customerFrame_txt.delete('1.0',END)
            self.customerFrame_txt.insert('1.0',bill_top_temp)

        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {str(es)}")


            
    def unpaid_bill_bottom(self):

        bill_bottom_temp=f'''
{str("="*45)}
 Bill Amount\t\t\t\tBDT.{self.bill_amount}
 Discount\t\t\t\tBDT.{self.discount}
 Net Pay\t\t\t\tBDT.{self.net_pay}
{str("="*45)}\n
UNPAID PAYMENT\n
PAID\t\t\t\t{self.var_paid.get()}BDT\n
        '''
        self.customerFrame_txt.insert(END,bill_bottom_temp)


          
    def unpaid_bill_middle(self):
    
        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            for row in self.cart_list:
            # pid,name,mrp, dp,qty,stock
                p_id = row[0]
                name= row[1]
                qty=int(row[5])-int(row[4])
                # qty=int(row[4])-int(row[3])

                if int(row[4])==int(row[5]):
                    status = 'Inactive'

                if int(row[4])!=int(row[5]):
                    status = 'Active'

                mrp=float(row[2])*int(row[4])
                mrp=str(mrp)
                self.customerFrame_txt.insert(END,"\n "+name+"\t\t\t"+row[4]+"\tBDT."+mrp)


        #   =-=============  update quantity in product table   ======================
                cur.execute("Update product set qty=?, status=? where p_id=?",(
                    qty,
                    status,
                    p_id,
                ))

                con.commit()
            con.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)

                    


    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_mrp.set('')
        self.var_qty.set('')
        self.instock.config(text=(f"In Stock"))
        self.var_stock.set('row[4]')


    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set("")
        self.var_contact.set("")
        self.customerFrame_txt.delete("1.0", END)
        self.cartFrame_lbl.config(text=f"CART\t Total products - 0")
        self.var_search.set("")
        
        self.clear_cart()
        self.show()
        self.show_cart()


    def update_date_time(self):
        con = sqlite3.connect(database =r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")

            self.clock_label.config(text=f"Welcome to {name} \t\t\t {time_} \t\t\t {date_}")
            self.clock_label.after(200, self.update_date_time)

        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)



    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print', "Please wait while printing", parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.customerFrame_txt.get('1.0', END))
            os.startfile(new_file, 'print')

        else:
            messagebox.showerror('Error', "Please generate bill to print the receipt.", parent=self.root)



    def logout(self):
        self.root.destroy()
        os.system("python login.py")
            


if __name__ == "__main__":
    root= Tk()
    obj = billinngClass(root)
    root.mainloop()