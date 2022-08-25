from email import message
from email.mime import image
from re import L
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from turtle import color, left, onclick
import sqlite3
import create_db 


class supplierClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1000x582+255+120')
        self.root.config(bg="#000229")
        self.root.iconbitmap('images/icon.ico')
        self.root.focus_force()
        self.root.title("SMART SHOP | PRODUCT OF exeyezone")


    #=====================================================================================================

    #===============  All Variables   =================

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_sup_invoice = StringVar()
        self.var_contactno = StringVar()
        self.var_name = StringVar()
        self.var_txt_desc = StringVar()




    # ====================  heading in self frame   =======================
        heading_label = Label(self.root, text="SUPPLIER DETAILS",font=("Montserrat", 20, "bold") , bg="#b4fcde", fg="#233233")
        heading_label.place(x=28, y=10, width=1000, height=35)


    # ===========================    search Frame   ===========================
        search_frame=LabelFrame(self.root, text="  SEARCH SUPPLIER  ", font=("Montserrat",9, "bold"), bg="#002e50", fg="white", bd=2)
        search_frame.place(x=28, y=55, width=600, height=70)

        # ======================     Options    ======================
        lbl_search = Label(search_frame,text="Search by invoice no.",bg="#002e50", fg="white" , font=("Montserrat", 11, "bold"))
        lbl_search.place(x=10, y=10)


        # ====================== Entry box and search button in Search frame =======================
        search_entry=Entry(search_frame, text=("Montserrat", 11),textvariable=self.var_searchtxt ,bg="lightyellow", fg="black", relief=FLAT, bd=2)
        search_entry.place(x=200, y=10, width=250, height=25)

        self.search_btn=PhotoImage(file="images/search.png")
        search_btn=Button(search_frame,command=self.search, image=self.search_btn, bg="#002e50", relief=FLAT, activebackground="#002e50", bd=0)
        search_btn.place(x=460, y=0)



    # content in self.root Frame
    
        #Label
        lbl_sup_invoice= Label(self.root, text="Invoice No", font=("Montserrat", 13), bg="#000229", fg="white")
        lbl_contact= Label(self.root, text="Contact", font=("Montserrat", 13), bg="#000229", fg="white")
        lbl_name= Label(self.root, text="Name", font=("Montserrat", 13), bg="#000229", fg="white")
        lbl_desc= Label(self.root, text="Description", font=("Montserrat", 13), bg="#000229", fg="white")


        # Entry Label
        entry_sup_invoice = Entry(self.root, textvariable=self.var_sup_invoice, relief=FLAT, font=("Montserrat", 13), bd=2, bg="#27ffff", fg="#263233")
        entry_contactno = Entry(self.root, textvariable=self.var_contactno, relief=FLAT, font=("Montserrat", 13), bd=2, bg="#27ffff", fg="#263233")
        entry_name = Entry(self.root, textvariable=self.var_name, relief=FLAT, font=("Montserrat", 13), bd=2, bg="#27ffff", fg="#263233")
        self.txt_desc = Text(self.root, relief=FLAT, font=("Montserrat", 13), bd=2, bg="#27ffff", fg="#263233")


        # Entry Label Place
        entry_sup_invoice.place(x=160, y=160, width=170)
        entry_name.place(x=160, y=210, width=170)
        entry_contactno.place(x=160, y=260, width=170)
        self.txt_desc.place(x=160, y=310, width=470, height=80)

        
        #Label place
        lbl_sup_invoice.place(x=50, y=160)
        lbl_name.place(x=50, y=210)
        lbl_contact.place(x=50, y=260)
        lbl_desc.place(x=50, y=310)



        # ==========================     Button for form      ============================
        self.save_btn = PhotoImage(file="images/save_btn.png")
        save_btn = Button(self.root, image=self.save_btn, command=self.add, relief=FLAT, bg="#000229", cursor="hand2", activebackground="#000229", bd=0)
        save_btn.place(x=50, y=450)

        self.update_btn = PhotoImage(file="images/update_btn.png")
        update_btn = Button(self.root, image=self.update_btn, command=self.update, relief=FLAT, bg="#000229", cursor="hand2", activebackground="#000229", bd=0)
        update_btn.place(x=200, y=450)

        self.delete_btn = PhotoImage(file="images/delete_btn.png")
        delete_btn = Button(self.root,command=self.delete, image=self.delete_btn, relief=FLAT, bg="#000229", cursor="hand2", activebackground="#000229", bd=0)
        delete_btn.place(x=350, y=450)

        self.clear_btn = PhotoImage(file="images/clear_btn.png")
        clear_btn = Button(self.root,command=self.clear, image=self.clear_btn, relief=FLAT, bg="#000229", cursor="hand2", activebackground="#000229", bd=0)
        clear_btn.place(x=500, y=450)



    # supplier  Frame and details
        sup_frame = Frame(self.root, bd=2, relief=RIDGE )
        sup_frame.place(x=650, y=55, width=350, height=420)

        scrolly = Scrollbar(sup_frame, orient=VERTICAL)
        scrollx = Scrollbar(sup_frame, orient=HORIZONTAL)

        self.supplierTable= ttk.Treeview(sup_frame, columns=("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)
        scrolly.config(command=self.supplierTable.yview)
        scrollx.config(command=self.supplierTable.xview)

        self.supplierTable.heading('invoice', text="INVOICE")
        self.supplierTable.heading('name', text="Name")
        self.supplierTable.heading('contact', text="Contact")
        self.supplierTable.heading('desc', text="Description")

        self.supplierTable["show"]="headings"

        self.supplierTable.column('invoice', width=90)
        self.supplierTable.column('name', width=100)
        self.supplierTable.column('contact', width=100)
        self.supplierTable.column('desc', width=100)

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()




#=======================================================    FUNCTION ARE FROM HERE  ==============================================================================================

    def add(self):

        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice must be required.", parent=self.root)

            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("error", "This invoice number is already satisfied. Try another one!")

                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, desc) VALUES(?,?,?,?)", (

                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contactno.get(),
                        self.txt_desc.get('1.0', END),
                    
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added Successfully", parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)


    def show(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {str(ex)}")

    
    def get_data(self, env):
        f= self.supplierTable.focus()
        content = self.supplierTable.item(f)
        row = content['values']

        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contactno.set(row[2]),
        self.txt_desc.delete('1.0', END),
        self.txt_desc.insert(END, row[3]),
        
        

    def update(self):

        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice must be requied", parent=self.root)

            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("error", "Invalid Invoice no")

                else:
                    cur.execute("Update supplier set name=?, contact=?, desc=? where invoice=?",  (

                        
                        self.var_name.get(),
                        self.txt_desc.get('1.0', END),
                        self.var_contactno.get(),
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)


    def delete(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()

        try:

            if self.var_sup_invoice=="":
                messagebox.showerror("Error", "Invoice no must be required.", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                cur.fetchone()

                if self.var_sup_invoice == NONE:
                    messagebox.showerror("Error", "Invalid Invoice", parent=self.root)
                else:
                    op = messagebox.askyesno("CONFARMATION", "Do you really want to delete supplier?", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier Successfully deleted", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {(ex)}", parent=self.root)
        


    def clear(self):

        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contactno.set(""),
        self.txt_desc.delete('1.0', END),
        self.var_searchtxt.set("")

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
                cur.execute("Select * from supplier where invoice=?", (self.var_searchtxt.get(), ))
                row=cur.fetchone()
                if row!=0:
                    self.supplierTable.delete(*self.supplierTable.get_children()) 
                    self.supplierTable.insert('', END, values=row)
                
                else:
                    messagebox.showerror("Error", "Result not found!!!", parent=self.root)
                con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {(ex)}", parent=self.root)





if __name__ == "__main__":
    root= Tk()
    obj = supplierClass(root)
    root.mainloop()