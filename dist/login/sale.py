from distutils.cmd import Command
from email import message
from email.mime import image
from re import L
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from tkinter import font
from tokenize import String
from turtle import color, left, onclick
import sqlite3
import os
from unicodedata import category
from pkg_resources import ContextualVersionConflict
from requests import delete
import create_db 
from billing import billinngClass






class salesClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1000x582+255+130')
        self.root.config(bg="#062936")
        self.root.focus_force()
        self.root.iconbitmap('images/icon.ico')
        self.root.title("All Sells Report  |  SMART SHOP | PRODUCT OF exeyezone")


        # variable
        self.var_searchby = StringVar()
        self.bill_list = []
        self.var_invoice= StringVar()


        # ======================== Self root frame title ========================
        heading_label = Label(self.root, text="CUSTOMER BILL REPORTS",font=("montserrat", 17, "bold") , bg="#b4fcde", fg="#233233")
        heading_label.place(x=10, y=10, width=980)




# ===========================    search Frame   ===========================
        search_frame=LabelFrame(self.root, text="   Search Invoice   ", font=("Montserrat",12, "bold"), bg="#113745", fg="white", bd=2)
        search_frame.place(x=10, y=55, width=710, height=70)

        # ====================== Entry box and search button in Search frame =======================
        search_lbl = Label(search_frame, text="Invoice No",font=("Montserrat", 12, "bold") , bg="#113745", fg="white")
        search_lbl.place(x=20, y=5)

        search_entry=Entry(search_frame, text=("Montserrat", 13),textvariable=self.var_invoice ,bg="lightyellow", fg="black", relief=FLAT, bd=2)
        search_entry.place(x=140, y=10, width=250, height=25)

        self.search_btn=PhotoImage(file="images/search.png")
        search_btn=Button(search_frame, image=self.search_btn,command=self.search, bg="#113745", relief=FLAT)
        search_btn.place(x=420, y=0)

        self.clear_btn=PhotoImage(file="images/clear_btn.png")
        clear_btn=Button(search_frame, image=self.clear_btn,command=self.clear , bg="#113745", relief=FLAT)
        clear_btn.place(x=560, y=5)

        self.new_sells_btn=PhotoImage(file="images/new_sells_btn.png")
        new_sells_btn_btn=Button(self.root, image=self.new_sells_btn, command=self.billing,cursor="hand2" , bg="#062936", relief=FLAT, bd=0, activebackground="#062936")
        new_sells_btn_btn.place(x=760, y=68)

        


# =======================      Bill list Frame     =========================
        sales_list_Frame = Listbox(self.root,relief=FLAT, bg="#113745", fg="white")
        sales_list_Frame.place(x=10, y=150, width=280, height=400)

        yscroll = Scrollbar(sales_list_Frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_list_Frame, bg="#113745", fg="white", font=("Montserrat", 13), yscrollcommand=yscroll.set)
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.sales_list.yview)
        
        self.sales_list.pack(fill=BOTH, expand=1)

        self.sales_list.bind("<ButtonRelease-1>", self.get_data)

        

# =======================      Bill Area     =========================

        bill_Frame = Listbox(self.root,relief=FLAT, bg="#113745", fg="white")
        bill_Frame.place(x=320, y=150, width=400, height=400)

        bill_frame_heading= Label(bill_Frame, text="CUSTOMER BILLING AREA", bg="#113745", fg="white", font=("arial", 12))
        bill_frame_heading.pack(side=TOP, expand=1,pady=5)

        yscroll2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, bg="lightyellow", fg="#113745", font=("Montserrat", 10), yscrollcommand=yscroll2.set)
        yscroll2.pack(side=RIGHT, fill=Y)
        yscroll2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=1)

        self.show()

# =======================   Function are here   =========================

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        # print(os.listdir("bill"))
        for i in os.listdir('bill'):
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])
    

    def get_data(self, ev):
        index_ = self.sales_list.curselection()
        file_name = self.sales_list.get(index_)
        # print(file_name)
        self.bill_area.delete("1.0", END)
        fp = open(f'bill/{file_name}', 'r')
        for i in fp:
            self.bill_area.insert(END, i)
            
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error", "Invoice No. should be required.", parent=self.root)

        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f'bill/{self.var_invoice.get()}.txt', 'r')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Error", "Invalid Invoice number. Try again", parent=self.root)

    
    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)


    '''def new_sells(self):
        os.system("python billing.py")'''

        
    def billing(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = billinngClass(self.new_win)





if __name__ == "__main__":
    root= Tk()
    obj = salesClass(root)
    root.mainloop()