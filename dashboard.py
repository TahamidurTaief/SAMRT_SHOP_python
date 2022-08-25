from email import message
from email.mime import image
from tkinter import *
from tkinter import messagebox
from turtle import color, left, onclick
import sqlite3
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sale import salesClass
from settings import settingClass
from about import aboutClass
from login import loginClass
from billing import billinngClass
import create_db 
import os
import time


class YMS:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1300x770+0+0')
        self.root.config(bg="#10213B")
        self.root.title("SMART SHOP | PRODUCT OF exeyezone")
        self.root.iconbitmap('images/icon.ico')




    # ==============  title of main frame  ==============
        con = sqlite3.connect(database =r"yms.db")
        cur = con.cursor()
        try:
            
            self.root.icon_title=PhotoImage(file="images/title_bar.png")
            title=Label(self.root,image=self.root.icon_title)
            title.place(x=0, y=0, relwidth=1)
            
            cur.execute("SELECT name FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]
            title_lbl = Label(self.root, text=f"{name}", font=("Montserrat", 19, "bold"), relief=FLAT, bg="#1D2142", fg= "#ffac48")
            title_lbl.place(x=300, y=12)

            con.commit()
            cur.close()

        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {es}")



    #  ============== logout button  ==============

        self.setting_btn = PhotoImage(file="images/setting_icon.png")
        setting_btn=Button(self.root, image=self.setting_btn,command=self.settings, bg="#1D2142", bd=0, cursor="hand2", activebackground="#1D2142")
        setting_btn.place(x=1220, y=15)

        self.about_btn = PhotoImage(file="images/about_us.png")
        about_btn=Button(self.root, image=self.about_btn,command=self.about_us, bg="#1D2142", bd=0, cursor="hand2", activebackground="#1D2142")
        about_btn.place(x=1170, y=15)

        self.root.logout_btn = PhotoImage(file="images/singout.png")
        logout_btn=Button(self.root, image=self.root.logout_btn,command=self.logout, bg="#1D2142", bd=0, cursor="hand2", activebackground="#1D2142")
        logout_btn.place(x=1020, y=10)


    # ==============  Clock Label  ==============
        self.clock_label=Label(self.root, text="Welcome to Smart Shop \t\t\t\t DD:MM:YY \t\t\t\t SS:MM:HH", font=("Montserrat", 15), bg="#245e5b", fg="white")
        self.clock_label.place(x=0, y=55, relwidth=1)


    #============== Left Menu ==============
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="#0f1b2c")
        LeftMenu.place(x=0, y=90, width=250, height=650)


        # ============== Left Menu Image============== 
        self.LeftMenu_bg=PhotoImage(file="images/LeftMenu_top_img.png")
        LeftMenu_img=Label(LeftMenu, image=self.LeftMenu_bg, bg="#0f1b2c")
        LeftMenu_img.place(x=5, y=5)

        # Menu Lable
        label_menu = Label(LeftMenu, text="Menu", font=("Montserrat", 20, "bold"), bg="#245e5b", fg="white")
        label_menu.place(x=0, y=220, relwidth=1)


    # ============== Menu Button ==============

    
        self.root.emp_btn = PhotoImage(file="images/employee_btn.png")
        emp_btn=Button(LeftMenu, image=self.root.emp_btn,activebackground="#4dbbff", activeforeground="#191629", command=self.employee, bd=0,bg="#0f1b2c", cursor="hand2", relief=FLAT)
        emp_btn.place(x=0, y=270, relwidth=1)

        self.root.supplier_btn = PhotoImage(file="images/supplier_btn.png")
        supplier_btn=Button(LeftMenu, image=self.root.supplier_btn,activebackground="#4dbbff", activeforeground="#191629",  command=self.supplier ,bd=0,bg="#0f1b2c", cursor="hand2", relief=FLAT)
        supplier_btn.place(x=0, y=330, relwidth=1)

        self.root.category_btn = PhotoImage(file="images/category.png")
        category_btn=Button(LeftMenu, image=self.root.category_btn,activebackground="#4dbbff", activeforeground="#191629",  command=self.category, bd=0,bg="#0f1b2c", cursor="hand2", relief=FLAT)
        category_btn.place(x=0, y=390, relwidth=1)

        self.products_btn = PhotoImage(file="images/products_btn.png")
        products_btn=Button(LeftMenu, image=self.products_btn,activebackground="#4dbbff", activeforeground="#191629", command=self.product, bg="#0f1b2c" , bd=0, cursor="hand2", relief=FLAT)
        products_btn.place(x=0, y=450, relwidth=1)

        self.root.sales_btn = PhotoImage(file="images/sales.png")
        sales_btn=Button(LeftMenu, image=self.root.sales_btn,activebackground="#4dbbff", activeforeground="#191629", command=self.sale , bd=0,bg="#0f1b2c", cursor="hand2", relief=FLAT)
        sales_btn.place(x=0, y=510, relwidth=1)

        self.root.exit_btn = PhotoImage(file="images/exit.png")
        exit_btn=Button(LeftMenu, image=self.root.exit_btn,activebackground="#4dbbff", activeforeground="#191629", command=self.exit, bd=0 ,bg="#0f1b2c", cursor="hand2", relief=FLAT)
        exit_btn.place(x=0, y=570, relwidth=1)


    # ==============  Banner image  ==============
        self.employee_banner=PhotoImage(file="images/banner.png")
        self.lebel_employee=Label(self.root, image=self.employee_banner, relief=FLAT, bg="#10213B")
        self.txt_label_employee=Label(self.root, text="Total Employee\n[ 0 ]",bg="#91F3CA", fg="#1D2142", font=("Montserrat", 15, "bold"))
        self.txt_label_employee.place(x=338,y=200)
        self.lebel_employee.place(x=300, y=120)

        self.supplier_banner=PhotoImage(file="images/banner.png")
        self.lebel_supplier=Label(self.root, image=self.supplier_banner, relief=FLAT, bg="#10213B")
        self.txt_label_supplier=Label(self.root, text="Total Supplier\n[ 0 ]",bg="#91F3CA", fg="#1D2142", font=("Montserrat", 15, "bold"))
        self.txt_label_supplier.place(x=690,y=200)
        self.lebel_supplier.place(x=650, y=120)

        self.product_banner=PhotoImage(file="images/banner.png")
        self.lebel_product=Label(self.root, image=self.product_banner, relief=FLAT, bg="#10213B")
        self.txt_label_product=Label(self.root, text="Total Product\n[ 0 ]",bg="#91F3CA", fg="#1D2142", font=("Montserrat", 15, "bold"))
        self.txt_label_product.place(x=1050,y=200)
        self.lebel_product.place(x=1000, y=120)

        self.category_banner=PhotoImage(file="images/banner.png")
        self.lebel_category=Label(self.root, image=self.category_banner, relief=FLAT, bg="#10213B")
        self.txt_label_category=Label(self.root, text="Total Category\n[ 0 ]",bg="#91F3CA", fg="#1D2142", font=("Montserrat", 15, "bold"))
        self.txt_label_category.place(x=340,y=375)
        self.lebel_category.place(x=300, y=300)


        self.sells_banner=PhotoImage(file="images/banner.png")
        self.lebel_sells=Label(self.root, image=self.sells_banner, relief=FLAT, bg="#10213B")
        self.txt_label_sells=Label(self.root, text="Total Sells\n[ 0 ]",bg="#91F3CA", fg="#1D2142", font=("Montserrat", 15, "bold"))
        self.txt_label_sells.place(x=720,y=375)
        self.lebel_sells.place(x=650, y=300)


        
        self.employee_icon=PhotoImage(file="images/employee_icon.png")
        lebel_employee=Label(self.root, image=self.employee_icon, relief=FLAT, bg="#91f3ca")
        lebel_employee.place(x=390,y=130)

        self.supplier_icon=PhotoImage(file="images/supplier_icon.png")
        lebel_supplier=Label(self.root, image=self.supplier_icon, relief=FLAT, bg="#91f3ca")
        lebel_supplier.place(x=730,y=130)

        self.product_icon=PhotoImage(file="images/product_icon.png")
        lebel_product=Label(self.root, image=self.product_icon, relief=FLAT, bg="#91f3ca")
        lebel_product.place(x=1095,y=140)

        self.category_icon=PhotoImage(file="images/category_icon.png")
        lebel_category=Label(self.root, image=self.category_icon, relief=FLAT, bg="#91f3ca")
        lebel_category.place(x=390,y=315)

        self.sales_icon=PhotoImage(file="images/sales_icon.png")
        lebel_sales=Label(self.root, image=self.sales_icon, relief=FLAT, bg="#91f3ca")
        lebel_sales.place(x=750,y=315)


        # self.employee_banner=PhotoImage(file="images/employee_banner.png")
        # self.lebel_employee=Label(self.root, image=self.employee_banner, relief=FLAT)
        # self.txt_label_employee=Label(self.root, text="Total Employee\n[ 0 ]",bg="#FFDC11", fg="#1D2142", font=("Montserrat", 20, "bold"))
        # self.txt_label_employee.place(x=338,y=200)
        # self.lebel_employee.place(x=300, y=120)





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

                footer = Label(self.root, text=f"{name} |  PRODUCT OF exeyezone \n website: www.exeyezone.com      |      email: exeyezoneltd@gmail.com      |      Contact: 01977794509", font=("Montserrat", 9), bg="#245e5b", fg="white")
                footer.pack(side=BOTTOM, fill=X)
            con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)

        self.update_content()
        

    #==========================================================================================================
    def employee(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def sale(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def settings(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = settingClass(self.new_win)
    
    def about_us(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = aboutClass(self.new_win)

    def login(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = loginClass(self.new_win)

    def billing(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = billinngClass(self.new_win)



    def update_content(self):
        con = sqlite3.connect(database=r'yms.db')
        cur = con.cursor()
        try:
            cur.execute('SELECT * FROM product')
            product=cur.fetchall()
            self.txt_label_product.config(text=f"Total Product\n[ {str(len(product))} ]")

            cur.execute('SELECT * FROM supplier')
            supplier=cur.fetchall()
            self.txt_label_supplier.config(text=f"Total Suppliers\n[ {str(len(supplier))} ]")

            cur.execute('SELECT * FROM catagory')
            category=cur.fetchall()
            self.txt_label_category.config(text=f"Total Category\n[ {str(len(category))} ]")

            cur.execute('SELECT * FROM employee')
            employee=cur.fetchall()
            self.txt_label_employee.config(text=f"Total Employee\n[ {str(len(employee))} ]")


            self.txt_label_sells.config(text=f"Total Sales\n[ {str(len(os.listdir('bill')))} ]")

            # def update_date_time(self):
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
                self.clock_label.after(200, self.update_content)

            except Exception as ex:
                messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)
            


        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {str(es)}")


    

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def exit(self):
        self.root.destroy()


        


if __name__ == "__main__":
    root= Tk()
    obj = YMS(root)
    root.mainloop()