from email import message
from email.mime import image
from re import L
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from turtle import color, left, onclick
import sqlite3
from unicodedata import category
from pkg_resources import ContextualVersionConflict
import qrcode
import create_db 
from PIL import Image, ImageTk



class productClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1000x582+255+130')
        self.root.config(bg="#062936")
        self.root.focus_force()
        self.root.iconbitmap('images/icon.ico')
        self.root.title("Product Control  |  SMART SHOP | PRODUCT OF exeyezone")


        self.var_p_id = StringVar()
        self.var_category=StringVar()
        self.var_supplier = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_category_supplier()
        self.var_name = StringVar()
        self.var_mrp = StringVar()
        self.var_dp = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        self.var_searchtxt = StringVar()
        self.var_searchby = StringVar()

# =================================     Product Details Frame      ==================================
        productFrame = Frame(self.root, bg="#113745", relief=RIDGE, bd=2)
        productFrame.place(x=10, y=10, width=450, height=560)

    # ======== Product Details Label ==========
        product_title = Label(productFrame, text="PRODUCT DETAILS", bg="#bafee2", fg="#10213b", font=("Montserrat", 15, "bold"))
        product_title.place(x=0, y=10, relwidth=1)


    # Label in productFrame

        product_id_lbl = Label(productFrame, text="Product ID", bg="#113745", fg="white", font=("Montserrat", 18))
        product_id_lbl.place(x=10, y=50)

        category_lbl = Label(productFrame, text="Catagory", bg="#113745", fg="white", font=("Montserrat", 18))
        category_lbl.place(x=10, y=100)

        supplier_lbl = Label(productFrame, text="Supplier", bg="#113745", fg="white", font=("Montserrat", 18))
        supplier_lbl.place(x=10, y=150)

        name_lbl = Label(productFrame, text="Name", bg="#113745", fg="white", font=("Montserrat", 18))
        name_lbl.place(x=10, y=200)

        mrp_lbl = Label(productFrame, text="MRP", bg="#113745", fg="white", font=("Montserrat", 18))
        mrp_lbl.place(x=10, y=250)

        dp_lbl = Label(productFrame, text="DP", bg="#113745", fg="white", font=("Montserrat", 18))
        dp_lbl.place(x=10, y=300)

        qty_lbl = Label(productFrame, text="QTY", bg="#113745", fg="white", font=("Montserrat", 18))
        qty_lbl.place(x=10, y=350)

        status_lbl = Label(productFrame, text="Status", bg="#113745", fg="white", font=("Montserrat", 18))
        status_lbl.place(x=10, y=400)

    # Entry in productFrame

        product_id_entry = Entry(productFrame, bg="#74dffe",textvariable=self.var_p_id, fg= "#062936", font=("Montserrat", 15))
        product_id_entry.place(x=150, y=55, width=250)

        cmd_category = ttk.Combobox(productFrame,textvariable=self.var_category , values=self.cat_list, state='readonly', justify=CENTER, font=("Montserrat", 15))
        cmd_category.place(x=150, y=100, width=250)
        cmd_category.current(0)

        cmd_suplier = ttk.Combobox(productFrame,textvariable=self.var_supplier , values=self.sup_list, state='readonly', justify=CENTER, font=("Montserrat", 15))
        cmd_suplier.place(x=150, y=150, width=250)
        cmd_suplier.current(0)

        name_entry = Entry(productFrame, bg="#74dffe",textvariable=self.var_name, fg= "#062936", font=("Montserrat", 15))
        name_entry.place(x=150, y=200, width=250)

        mrp_entry = Entry(productFrame, bg="#74dffe", textvariable=self.var_mrp, fg= "#062936", font=("Montserrat", 15))
        mrp_entry.place(x=150, y=250, width=250)

        dp_entry = Entry(productFrame, bg="#74dffe", textvariable=self.var_dp, fg= "#062936", font=("Montserrat", 15))
        dp_entry.place(x=150, y=300, width=250)

        qty_entry = Entry(productFrame, bg="#74dffe", textvariable=self.var_qty,  fg= "#062936", font=("Montserrat", 15))
        qty_entry.place(x=150, y=350, width=250)

        cmd_search = ttk.Combobox(productFrame,textvariable=self.var_status , values=("Select", "Active", "Inactive"), state='readonly', justify=CENTER, font=("Montserrat", 15))
        cmd_search.place(x=150, y=400, width=250)
        cmd_search.current(0)

    # Buttons
        self.save_btn = PhotoImage(file="images/save_btn.png")
        save_btn = Button(productFrame, image=self.save_btn, bd=0,command=self.add,activebackground="#113745", bg="#113745" , relief=FLAT, cursor="hand2")
        save_btn.place(x=10, y=465)

        self.delete_btn = PhotoImage(file="images/delete_btn.png")
        delete_btn = Button(productFrame, image=self.delete_btn, bd=0,command=self.delete ,activebackground="#113745", bg="#113745" , relief=FLAT, cursor="hand2")
        delete_btn.place(x=160, y=465)

        self.update_btn = PhotoImage(file="images/update_btn.png")
        update_btn = Button(productFrame, image=self.update_btn, bd=0,command=self.update ,activebackground="#113745", bg="#113745" , relief=FLAT, cursor="hand2")
        update_btn.place(x=310, y=465)

        self.clear_btn = PhotoImage(file="images/clear_btn.png")
        clear_btn = Button(productFrame, image=self.clear_btn, bd=0,command=self.clear ,activebackground="#113745", bg="#113745" , relief=FLAT, cursor="hand2")
        clear_btn.place(x=160, y=515)



# ===========================    search Frame   ===========================
        search_frame=LabelFrame(self.root, text="Search Products", font=("Montserrat",10, "bold"), bg="#113745", fg="white", bd=2)
        search_frame.place(x=480, y=10, width=500, height=70)        

# ====================== Entry box and search button in Search frame =======================
        cmd_search = ttk.Combobox(search_frame,textvariable=self.var_searchby , values=("Select", "Category", "Supplier", "name"), state='readonly', justify=CENTER, font=("Montserrat", 15))
        cmd_search.place(x=10, y=10, width=120)
        cmd_search.current(0)

        search_entry=Entry(search_frame, text=("Montserrat", 13),textvariable=self.var_searchtxt ,bg="lightyellow", fg="black", relief=FLAT, bd=2)
        search_entry.place(x=150, y=10, width=170, height=27)

        self.search_btn=PhotoImage(file="images/search.png")
        search_btn=Button(search_frame, image=self.search_btn, command=self.search, bg="#113745", relief=FLAT)
        search_btn.place(x=350, y=0)


# product Tree View Frame and details
        prod_frame = Frame(self.root, bd=2, relief=RIDGE )
        prod_frame.place(x=480, y=100, width=500, height=255)

        scrolly = Scrollbar(prod_frame, orient=VERTICAL)
        scrollx = Scrollbar(prod_frame, orient=HORIZONTAL)

        self.productTable= ttk.Treeview(prod_frame, columns=("p_id", "Category", "Supplier", "name", "mrp","dp", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)
        scrolly.config(command=self.productTable.yview)
        scrollx.config(command=self.productTable.xview)

        self.productTable.heading('p_id', text="P ID")
        self.productTable.heading('Category', text="Category")
        self.productTable.heading('Supplier', text="Supplier")
        self.productTable.heading('name', text="Name")
        self.productTable.heading('mrp', text="MRP")
        self.productTable.heading('dp', text="DP")
        self.productTable.heading('qty', text="QTY")
        self.productTable.heading('status', text="Status")

        self.productTable["show"]="headings"

        self.productTable.column('p_id', width=50)
        self.productTable.column('Category', width=100)
        self.productTable.column('Supplier', width=100)
        self.productTable.column('name', width=100)
        self.productTable.column('mrp', width=100)
        self.productTable.column('dp', width=100)
        self.productTable.column('qty', width=100)
        self.productTable.column('status', width=100) 

        self.productTable.pack(fill=BOTH, expand=1)
        self.productTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


# ===========================      QR CODE HERE        ===============================

        qr_frame=Frame(self.root, bg="#113745",relief=FLAT ,bd=3)
        qr_frame.place(x=480, y=365, width=500, height=200)


        self.qr_code_lbl = Label(qr_frame,text="No QR\nAvailable",  font=("Montserrat", 12), bg="#CFECEC", fg="#123456")
        self.qr_code_lbl.place(x=20, y=10, width=180, height=180)

    #======= Buttton here=======
        self.generate_btn = PhotoImage(file="images/generate_btn.png")
        self.qr_generate = Button(qr_frame, image=self.generate_btn,command=self.generate, bg="#113745", activebackground="#113745", bd=0)
        self.qr_generate.place(x=220, y=20)

#=============  logo in qr frame ===========
        logo_img = Image.open("images/exeyezone.png", 'r')
        resize_logo_img = logo_img.resize((200, 70))
        self.logo_img = ImageTk.PhotoImage(resize_logo_img)
        logo_img_exeyezone = Label(qr_frame, image=self.logo_img, bg="#113745")
        logo_img_exeyezone.place(x=250, y=95)


    # =========== QR Data
        

# ================================      All function are from here      ================================

    def generate(self):

        qr_data = (f"Catagory : {self.var_category.get()}\nSupplier : {self.var_supplier.get()}\nName : {self.var_name.get()}\nPrice : {self.var_mrp.get()}\nQTY : {self.var_qty.get()}\nStatus : {self.var_status.get()}")
        qr_code = qrcode.make(qr_data)
        print(qr_code)
        qr_code.save(f"product_qr/pro_"+str(self.var_name.get())+'.png')

    # ========= QR code image Update ========
        image = Image.open(f"product_qr/pro_"+str(self.var_name.get())+'.png', 'r')
        resize_image = image.resize((180, 180))
        self.im = ImageTk.PhotoImage(resize_image)
        self.qr_code_lbl.config(image=self.im)

        

        

        if self.var_category.get()=='' or self.var_category.get()=='' or self.var_supplier.get()=='' or self.var_name.get()=='' or self.var_mrp.get()=='' or self.var_qty.get()=='' or self.var_status.get()=='':
            messagebox.showerror("Error", "All fields should be required")

        else:
            messagebox.showinfo("Success", "Your Product details QR Code generated successful!")

    def fetch_category_supplier(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()
        
        try:
            cur.execute("SELECT cat_name FROM catagory")
            cat = cur.fetchall()
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])


            cur.execute("SELECT name FROM supplier")
            sup = cur.fetchall()
            
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")           
                for i in sup:
                    self.sup_list.append(i[0])


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)



    def add(self):

        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            if self.var_category.get()=="Select"or  self.var_category.get()=="Empty" or self.var_supplier == "Select" or self.var_name=="":
                messagebox.showerror("Error", "All fields should must be required.", parent=self.root)

            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("error", "This product is already satisfied. Try another one!", parent=self.root)

                else:
                    cur.execute("INSERT INTO product (p_id, Category ,  Supplier ,  name , mrp , dp ,  qty ,  status ) VALUES(?,?,?,?,?,?,?,?)", (
                        
                        self.var_p_id.get(),
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_mrp.get(),
                        self.var_dp.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Your product added Successfully", parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)


    def show(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {str(ex)}")



    def get_data(self, env):
        f= self.productTable.focus()
        content = self.productTable.item(f)
        row = content['values']

        self.var_p_id.set(row[0]),
        self.var_category.set(row[1]),
        self.var_supplier.set(row[2]),
        self.var_name.set(row[3]),
        self.var_mrp.set(row[4]),
        self.var_dp.set(row[5])
        self.var_qty.set(row[6]),
        self.var_status.set(row[7]),
        

    def update(self):

        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            if self.var_p_id.get()=="":
                messagebox.showerror("Error", "P ID must be requied", parent=self.root)

            else:
                cur.execute("SELECT * FROM product WHERE p_id=?", (self.var_p_id.get(), ))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("error", "Invalid Product Name")

                else:
                    cur.execute("Update product set Category=?,  Supplier=? ,  name=? ,  mrp=?, dp=? ,  qty=? ,  status=? WHERE p_id=?",  (

                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_mrp.get(),
                        self.var_dp.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_p_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)


    def delete(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()

        try:

            if self.var_p_id=="Select":
                messagebox.showerror("Error", "Select a product from the list.", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE p_id=?", (self.var_p_id.get(),))
                cur.fetchone()

                if self.var_p_id == NONE:
                    messagebox.showerror("Error", "Invalid Product Name", parent=self.root)
                else:
                    op = messagebox.askyesno("CONFARMATION", "Do you really want to delete this product?", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from product where p_id=?", (self.var_p_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Your product Successfully deleted", parent=self.root)
                        self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {(ex)}", parent=self.root)

    

    def clear(self):

        self.var_category.set("Select"),
        self.var_supplier.set("Select"),
        self.var_name.set(""),
        self.var_mrp.set(""),
        self.var_dp.set(""),
        self.var_qty.set(""),
        self.var_status.set("Select"),

        self.show()

    def search(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()

        try:

            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select search by option.", parent=self.root)
            
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search input should be requierd!", parent=self.root)

            else:
                cur.execute("Select * from product where "+ self.var_searchby.get()+" LIKE '%" +self.var_searchtxt.get()+"%'")
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
        






if __name__ == "__main__":
    root= Tk()
    obj = productClass(root)
    root.mainloop()