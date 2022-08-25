from email import message
from email.mime import image
from re import L
from sre_parse import CATEGORIES
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from turtle import color, left, onclick
import sqlite3
import create_db 


class categoryClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1000x582+255+130')
        self.root.config(bg="#1F2933")
        self.root.focus_force()
        self.root.iconbitmap('images/icon.ico')
        self.root.title("Your's Management System   |    PRODUCT CATEGORY   ")


        # All variables
        self.var_c_id = StringVar()
        self.var_cat_name = StringVar()



        
# ==========================     self frame      ============================

        # ===========   HEADING OF SELF FRAME   ============

        lbl_heading = Label(self.root, text="MANAGE CATEGORY PRODUCT", bg="#B4FCDE", fg= "#1F2933", font=("Montserrat", 18, "bold"))
        lbl_heading.place(x=0, y=15, relwidth=1)


# ==========   CATEGORY FRAME   =========

        category_frame = LabelFrame(self.root,text="CATEGORY" ,font=("Montserrat", 10) , bg="#1f3043", fg= "white")
        category_frame.place(x=20, y=70, width=600, height=120)


    
    # ===========     label and entry and buttons     ===========

        # label in category_frame
        lbl_category_name = Label(category_frame, text="Enter Category Name : ", font=("Montserrat",18), bg="#1f3043", fg="white")
        lbl_category_name.place(x=10, y=0)

        # Entry in category_frame
        entry_category=Entry(category_frame, bg="#BAEBE7",textvariable=self.var_cat_name , fg="#1F2933", font=("Montserrat", 12, "bold"))
        entry_category.place(x=10, y=50, width=300, height=31)

        # button in category_frame
        self.add_btn = PhotoImage(file="images/add_btn.png")
        add_btn = Button(category_frame, image=self.add_btn,command=self.add, relief=FLAT, cursor="hand2", bg="#1f3043")
        add_btn.place(x=325, y=49)

        self.delete_btn = PhotoImage(file="images/delete_catagory_btn.png")
        add_btn = Button(category_frame,command=self.delete , image=self.delete_btn, relief=FLAT, cursor="hand2", bg="#1f3043")
        add_btn.place(x=450, y=49)


# ===================       iMAGES HERE     ========================

        self.shop_poster1 = PhotoImage(file="images/shop_poster1.png")
        shop_poster1 = Label(self.root, image=self.shop_poster1, relief=FLAT, bg="#1F2933")
        shop_poster1.place(x=5, y=250)\

        self.shop_poster2 = PhotoImage(file="images/shop_poster2.png")
        shop_poster2 = Label(self.root, image=self.shop_poster2, relief=FLAT, bg="#1F2933")
        shop_poster2.place(x=550, y=270)

        under_img_lbl = Label(self.root, text="SMART SHOP   |   PRODUCT OF exeyezone.", font=("Montserrat", 13), bg="#1F2933", fg="#BAEBE7")
        under_img_lbl.place(x=320, y=550)

        

# ===================      TOTAL CATEGORIES FRAME AND TREEVIEW      ==================

        cat_treeview_frame = Frame(self.root, bd=2, relief=RIDGE)
        cat_treeview_frame.place(x=650, y=70, width=330, height=120)

        scrolly = Scrollbar(cat_treeview_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_treeview_frame, orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(cat_treeview_frame, columns=("c_id", "cat_name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)
        scrolly.config(command=self.categoryTable.yview)
        scrollx.config(command=self.categoryTable.xview)

        self.categoryTable.heading('c_id', text="C_ID")
        self.categoryTable.heading('cat_name', text="CAT_NAME")

        self.categoryTable["show"]="headings"

        self.categoryTable.column('c_id', width=50)
        self.categoryTable.column('cat_name', width=50)

        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()





# ============================      All Functions are form here     ===================================

    def add(self):

        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            if self.var_cat_name.get()=="":
                messagebox.showerror("Error", "Category name must be required.", parent=self.root)

            else:
                cur.execute("SELECT * FROM catagory WHERE cat_name=?", (self.var_cat_name.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("error", "This Category Name is already satisfied. Try another one!", parent=self.root)

                else:
                    cur.execute("INSERT INTO catagory (cat_name) VALUES(?)", (

                        self.var_cat_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Category added Successfully", parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)




    def show(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM catagory")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {str(ex)}")



    def get_data(self, env):
            f= self.categoryTable.focus()
            content = (self.categoryTable.item(f))
            row = content['values']

            self.var_c_id.set(row[0]),
            self.var_cat_name.set(row[1]),



    def delete(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()

        try:

            if self.var_c_id.get()=="":
                messagebox.showerror("Error", "Select Category Name from the list.", parent=self.root)
            else:
                cur.execute("SELECT * FROM catagory WHERE c_id=?", (self.var_c_id.get(),))
                cur.fetchone()

                if self.var_cat_name == NONE:
                    messagebox.showerror("Error", "Invalid Catagory Name. Please try again.", parent=self.root)
                else:
                    op = messagebox.askyesno("CONFARMATION", "Do you really want to delete this Category?", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from catagory where c_id=?", (self.var_c_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Category Successfully deleted", parent=self.root)
                        # self.clear()
                        self.show()
                        self.var_c_id.set("")
                        self.var_cat_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {(ex)}", parent=self.root)




if __name__ == "__main__":
    root= Tk()
    obj = categoryClass(root)
    root.mainloop()