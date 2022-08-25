from email import message
from email.mime import image
from re import L
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from turtle import color, left, onclick
import sqlite3
import create_db 


class employeeClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1000x582+255+130')
        self.root.config(bg="#10213b")
        self.root.focus_force()
        self.root.iconbitmap('images/icon.ico')
        self.root.title("SMART SHOP | PRODUCT OF exeyezone")


    #=====================================================================================================

    #===============  All Variables   =================

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contactno = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_usertype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()




    # ===========================    search Frame   ===========================
        search_frame=LabelFrame(self.root, text="Search Employee", font=("goudy old style",12, "bold"), bg="#334B4C", fg="white", bd=2)
        search_frame.place(x=250, y=20, width=600, height=70)

        # ======================     Options    ======================
        cmd_search = ttk.Combobox(search_frame,textvariable=self.var_searchby , values=("Select", "Name", "Email", "ID"), state='readonly', justify=CENTER, font=("goudy old style", 13))
        cmd_search.place(x=10, y=10, width=180)
        cmd_search.current(0)

        # ====================== Entry box and search button in Search frame =======================
        search_entry=Entry(search_frame, text=("Montserrat", 13),textvariable=self.var_searchtxt ,bg="lightyellow", fg="black", relief=FLAT, bd=2)
        search_entry.place(x=200, y=10, width=250, height=25)

        self.search_btn=PhotoImage(file="images/search.png")
        search_btn=Button(search_frame,command=self.search, image=self.search_btn, bg="#334B4C", relief=FLAT)
        search_btn.place(x=460, y=0)

    # ====================  heading in self frame   =======================
        heading_label = Label(self.root, text="Employee details",font=("goudy old style", 15) , bg="#b4fcde", fg="#233233")
        heading_label.place(x=28, y=110, width=950)

    # content in self.root Frame
        #Label
        lbl_emp_id= Label(self.root, text="Emp No", font=("goudy old style", 15), bg="#10213B", fg="white")
        lbl_gender= Label(self.root, text="Gender", font=("goudy old style", 15), bg="#10213B", fg="white")
        lbl_contact= Label(self.root, text="Contact", font=("goudy old style", 15), bg="#10213B", fg="white")

        lbl_name= Label(self.root, text="Name", font=("goudy old style", 15), bg="#10213B", fg="white")
        lbl_dob= Label(self.root, text="D.O.B", font=("goudy old style", 15), bg="#10213B", fg="white")
        lbl_doj= Label(self.root, text="D.O.J", font=("goudy old style", 15), bg="#10213B", fg="white")

        lbl_email= Label(self.root, text="Email", font=("goudy old style", 15), bg="#10213B", fg="white")
        lbl_password= Label(self.root, text="Password", font=("goudy old style", 15), bg="#10213B", fg="white")
        lbl_utype= Label(self.root, text="Usertype", font=("goudy old style", 15), bg="#10213B", fg="white")

        lbl_address= Label(self.root, text="Address", font=("goudy old style", 15), bg="#10213B", fg="white")
        lbl_salary= Label(self.root, text="Salary", font=("goudy old style", 15), bg="#10213B", fg="white")

        # Entry Label
        entry_emno = Entry(self.root, textvariable=self.var_emp_id, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")
        entry_gender= ttk.Combobox(self.root, values=("select", "Male", "Female"),state='readonly', textvariable=self.var_gender , font=("goudy old style", 15))
        entry_gender.current(0)
        entry_contactno = Entry(self.root, textvariable=self.var_contactno, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")

        entry_name = Entry(self.root, textvariable=self.var_name, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")
        
        entry_dob = Entry(self.root, textvariable=self.var_dob, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")
        entry_doj = Entry(self.root, textvariable=self.var_doj, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")

        entry_email = Entry(self.root, textvariable=self.var_email, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")
        entry_password = Entry(self.root, textvariable=self.var_password, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")
        
        entry_usertype = ttk.Combobox(self.root, values=("Select", "Admin", "Employee"),textvariable=self.var_usertype, font=("goudy old style", 15), state='readonly')
        entry_usertype.current(0)

        self.txt_address = Text(self.root, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")
        entry_salary = Entry(self.root, textvariable=self.var_salary, relief=FLAT, font=("goudy old style", 15), bd=2, bg="#B4FCDE", fg="#263233")




        # Entry Label Place
        entry_emno.place(x=160, y=160, width=170)
        entry_gender.place(x=460, y=160, width=170)
        entry_contactno.place(x=807, y=160, width=170)

        entry_name.place(x=160, y=210, width=170)
        entry_dob.place(x=460, y=210, width=170)
        entry_doj.place(x=807, y=210, width=170)

        entry_email.place(x=160, y=260, width=170)
        entry_password.place(x=460, y=260, width=170)
        entry_usertype.place(x=807, y=260, width=170)

        self.txt_address.place(x=160, y=310, width=300, height=80)
        entry_salary.place(x=580, y=310, width=170)

        
        #Label place
        lbl_emp_id.place(x=50, y=160)
        lbl_gender.place(x=350, y=160)
        lbl_contact.place(x=700, y=160)

        lbl_name.place(x=50, y=210)
        lbl_dob.place(x=350, y=210)
        lbl_doj.place(x=700, y=210)

        lbl_email.place(x=50, y=260)
        lbl_password.place(x=350, y=260)
        lbl_utype.place(x=700, y=260)

        lbl_address.place(x=50, y=310)
        lbl_salary.place(x=500, y=310)


        # ==========================     Button for form      ============================
        self.save_btn = PhotoImage(file="images/save_btn.png")
        save_btn = Button(self.root, image=self.save_btn, command=self.add, relief=FLAT, bg="#10213B", cursor="hand2")
        save_btn.place(x=500, y=350)

        self.update_btn = PhotoImage(file="images/update_btn.png")
        update_btn = Button(self.root, image=self.update_btn, command=self.update, relief=FLAT, bg="#10213B", cursor="hand2")
        update_btn.place(x=620, y=350)

        self.delete_btn = PhotoImage(file="images/delete_btn.png")
        delete_btn = Button(self.root,command=self.delete, image=self.delete_btn, relief=FLAT, bg="#10213B", cursor="hand2")
        delete_btn.place(x=740, y=350)

        self.clear_btn = PhotoImage(file="images/clear_btn.png")
        clear_btn = Button(self.root,command=self.clear, image=self.clear_btn, relief=FLAT, bg="#10213B", cursor="hand2")
        clear_btn.place(x=860, y=350)



    # Employee  Frame and details
        emp_frame = Frame(self.root, bd=2, relief=RIDGE )
        emp_frame.place(x=0, y=420, relwidth=1, height=168)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.employee_table= ttk.Treeview(emp_frame, columns=("eid", "name", "email", "address", "gender", "DOB", "password", "contact", 'DOJ', "user_type", "salary"), yscrollcommand=scrolly, xscrollcommand=scrollx)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)
        scrolly.config(command=self.employee_table.yview)
        scrollx.config(command=self.employee_table.xview)

        self.employee_table.heading('eid', text="EMP ID")
        self.employee_table.heading('name', text="Name")
        self.employee_table.heading('email', text="Email")
        self.employee_table.heading('address', text="Address")
        self.employee_table.heading('gender', text="Gender")
        self.employee_table.heading('DOB', text="DOB")
        self.employee_table.heading('password', text="Password")
        self.employee_table.heading('contact', text="Contact")
        self.employee_table.heading('DOJ', text="DOJ")
        self.employee_table.heading('user_type', text="User Type")
        self.employee_table.heading('salary', text="Salary")

        self.employee_table["show"]="headings"

        self.employee_table.column('eid', width=90)
        self.employee_table.column('name', width=100)
        self.employee_table.column('email', width=100)
        self.employee_table.column('address', width=100)
        self.employee_table.column('gender', width=100)
        self.employee_table.column('DOB', width=100)
        self.employee_table.column('password', width=100)
        self.employee_table.column('contact', width=100)
        self.employee_table.column('DOJ', width=100)
        self.employee_table.column('user_type', width=100)
        self.employee_table.column('salary', width=100)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()




#=======================================================    FUNCTION ARE FROM HERE  ==============================================================================================

    def add(self):

        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee Id must be required.", parent=self.root)

            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("error", "This Employee ID is already satisfied. Try another one!")

                else:
                    cur.execute("INSERT INTO employee (eid, name, email, address, gender, DOB, password, contact, DOJ, user_type, salary) VALUES(?,?,?,?,?,?,?,?,?,?,?)", (

                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.txt_address.get('1.0', END),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_password.get(),
                        self.var_contactno.get(),
                        self.var_doj.get(),
                        self.var_usertype.get(),
                        self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee added Successfully", parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)


    def show(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows=cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {str(ex)}")

    
    def get_data(self, env):
        f= self.employee_table.focus()
        content = self.employee_table.item(f)
        row = content['values']

        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.txt_address.delete('1.0', END),
        self.txt_address.insert(END, row[3]),
        self.var_gender.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_password.set(row[6]),
        self.var_contactno.set(row[7]),
        self.var_doj.set(row[8]),
        self.var_usertype.set(row[9]),
        self.var_salary.set(row[10]),
        

    def update(self):

        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be requied", parent=self.root)

            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("error", "Invalid Employee ID")

                else:
                    cur.execute("Update employee set name=?,  email=?,  address=?,  gender=?,  DOB=?,  password=?,  contact=?,  DOJ=?,  user_type=?,  salary=? where eid=?",  (

                        
                        self.var_name.get(),
                        self.var_email.get(),
                        self.txt_address.get('1.0', END),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_password.get(),
                        self.var_contactno.get(),
                        self.var_doj.get(),
                        self.var_usertype.get(),
                        self.var_salary.get(),
                        self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()


        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)


    def delete(self):
        con = sqlite3.connect(database=r"yms.db")
        cur = con.cursor()

        try:

            if self.var_emp_id=="":
                messagebox.showerror("Error", "Employee ID must be required.", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                cur.fetchone()

                if self.var_emp_id == NONE:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("CONFARMATION", "Do you really want to delete Employee ID?", parent=self.root)
                    if op == TRUE:
                        cur.execute("delete from employee where eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Employee ID Successfully deleted", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {(ex)}", parent=self.root)
        


    def clear(self):

        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.txt_address.delete('1.0', END),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_password.set(""),
        self.var_contactno.set(""),
        self.var_doj.set(""),
        self.var_usertype.set(""),
        self.var_salary.set(""),
        self.var_searchby.set("Select")
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
                cur.execute("Select * from employee where "+ self.var_searchby.get()+" LIKE '%" +self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for row in rows:
                        self.employee_table.insert('', END, values=row)
                
                else:
                    messagebox.showerror("Error", "Result not found!!!", parent=self.root)
                con.commit()
        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to {(ex)}", parent=self.root)





if __name__ == "__main__":
    root= Tk()
    obj = employeeClass(root)
    root.mainloop()