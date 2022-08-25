from email import message
from email.mime import image
from re import L
from sre_parse import State
from tkinter import *
from tkinter import messagebox, ttk
from turtle import back, color, left, onclick
import sqlite3
import os
from venv import create
from PIL import Image, ImageTk
import pymysql
import email_pass
import smtplib
import time
import create_db

from billing import billinngClass
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sale import salesClass
from settings import settingClass
from about import aboutClass
# from dashboard import YMS




class loginClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1350x770+0+0')
        self.root.iconbitmap('images/icon.ico')
        self.root.title("Login System | PRODUCT OF exeyezone")

        otp = ''


        self.background_img=PhotoImage(file="images/login_page_design.png")
        background_img = Label(self.root, image=self.background_img)
        background_img.place(x=0, y=0)


    # Variable=======
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_loginby = StringVar()


# ====================  Log in Frame and elements   =====================

    #=============log in Frame
        '''self.user_icon= PhotoImage(file="images/username_icon.png")
        user_icon = Label(self.root, image=self.user_icon, bg="#222531")
        user_icon.place(x=200, y=250)

        self.underline_icon= PhotoImage(file="images/uderline_icon.png")
        user_underline_icon = Label(self.root, image=self.underline_icon, bg="#222531")
        user_underline_icon.place(x=295, y=290)

        self.pass_icon= PhotoImage(file="images/password_icon.png")
        user_underline_icon = Label(self.root, image=self.pass_icon, bg="#222531")
        user_underline_icon.place(x=200, y=370)

        pass_underline_icon = Label(self.root, image=self.underline_icon, bg="#222531")
        pass_underline_icon.place(x=295, y=415)'''

        create_account = Label(self.root, text="Create Account  |", bg="#0E0438",fg="#E7E6E6", font=("Montserrat",12))
        create_account.place(x=215, y=620)

        forget_pass = Button(self.root, text="Forget Password",command=self.forget_windows , relief=FLAT, bd=0, cursor="hand2" , bg="#1F3D75",fg="#E7E6E6", font=("goury old style",11, "bold"), activebackground="#1F3D75", activeforeground="#E7E6E6")
        forget_pass.place(x=384, y=475)


    # =========   Entry of pass and user name

        user_entry = Entry(self.root, bg="#8598AA", bd=0,textvariable=self.var_username, fg="#FFFFFF", font=("Montserrat", 15, 'bold'))
        user_entry.place(x=215, y=306, width=298, height=60)

        pass_entry = Entry(self.root, bg="#8598AA", bd=0, fg="#FFFFFF", textvariable=self.var_password,show='*' , font=("Montserrat", 15, 'bold'))
        pass_entry.place(x=215, y=380, width=298, height=60)



        # hr_lbl = Label(self.root, bg="#35FDFF")
        # hr_lbl.place(x=240, y=580, width=400, height=2)

        # or_lbl = Label(self.root,text="OR", bg="#222531",fg="#35FDFF", font=("Montserrat",18))
        # or_lbl.place(x=410, y=565)


    # ========== Button
  
        self.login_btn = PhotoImage(file="images/login_button.png")
        login_btn = Button(self.root,image= self.login_btn, bg="#0F385A", fg="white",cursor="hand2", command=self.login , relief=FLAT, bd=0, activebackground="#8598AA", activeforeground="#0F385A")
        login_btn.place(x=150, y=525, width=360, height=60)

        singup_btn = Button(self.root, text="Sing UP", command=self.sing_up, fg="#E7E6E6",bg="#0E0438", cursor="hand2", bd=0, relief=FLAT ,font=("Montserrat",12, "bold"), activebackground="#0E0438", activeforeground="#48ffb8")
        singup_btn.place(x=356, y=618)


    # ============= Theam
        '''self.login_theam = PhotoImage(file="images/login_theam_design.png")     
        login_theam = Label(self.root, image=self.login_theam, bg="#222531", relief=FLAT, bd=0)
        login_theam.place(x=700, y=200)'''

        self.login_logo = PhotoImage(file="images/login_logo_design.png")     
        login_logo = Label(self.root, image=self.login_logo, bg="#0E0438", relief=FLAT, bd=0)
        login_logo.place(x=980, y=650, height=150, width=300)



    def login(self):

        '''if self.var_loginby.get()=='Admin':
            if self.var_username.get()=="" or self.var_password.get()=="":
                messagebox.showerror("Error", "Unsername and password mmust be required!")
            
            else:
                try:
                    con=pymysql.connect(host="localhost", user="root", passwd="", database='yms')
                    cur=con.cursor()
                    cur.execute("select * from yms_login where username=%s AND password=%s", (self.var_username.get(), self.var_password.get()))
                    row=cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "INVALID USERNAME AND PASSWORD")
                    else:
                        messagebox.showinfo("Success", "Sucessfylly loggin as Admin.")
                        self.root.destroy()
                        os.system("python dashboard.py")
                except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}")

        else:'''
        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        
        try:
            if self.var_username.get()=="" or self.var_password.get()=="":
                messagebox.showerror("Error", "Employee Id must be required.", parent=self.root)

            else:
                cur.execute("SELECT user_type FROM employee WHERE eid=? and password=?", (self.var_username.get(), self.var_password.get(),))
                user = cur.fetchone()
                if user==None:
                    messagebox.showerror("Error", "Invalid Username or Password.", parent=self.root)
                
                else:
                    if user[0]=="Admin":
                        # self.dashboard()
                        self.root.destroy()
                        os.system("python dashboard.py")
                        
                        messagebox.showinfo("Success", "Success to loggin as Admin!", parent=self.root)
                        
                    else:
                        
                        self.root.destroy()
                        # self.billing()
                        os.system("python billing.py")
                        messagebox.showinfo("Success", "Success to loggin as Employee!", parent=self.root)


        except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)




    def forget_windows(self):
        con=sqlite3.connect(database =r"yms.db")
        cur=con.cursor()
        if self.var_username.get()=='':
            messagebox.showerror("Error", "Enployee ID must be required.")
        
        else:
            cur.execute("SELECT email FROM employee WHERE eid=?", (self.var_username.get(),))
            email = cur.fetchone()
            if email==None:
                messagebox.showerror("Error", "Invalid Employee Id! Try with another one.")
            
            else:

                self.var_otp = StringVar()
                self.var_new_pass = StringVar()
                self.var_confirm_pass = StringVar()

                # Forget Password WIndow Generate
                
                chk = self.send_email(email[0])
                if chk=='f':
                    messagebox.showerror("Error", "Connection Error, try again!", parent=self.root)
                
                else:

                    self.forget_win = Toplevel(self.root)
                    self.forget_win.title("Reset Password")
                    self.forget_win.geometry("600x400+600+200")
                    self.forget_win.focus_force()

                    self.forget_frame_img = PhotoImage(file="images/forget_pasword_frame.png")
                    forget_frame_img = Label(self.forget_win, image=self.forget_frame_img)
                    forget_frame_img.place(x=0,y=0)

                    self.submit_btn = PhotoImage(file="images/submit_btn.png")
                    self.submit = Button(self.forget_win, command=self.validate_otp, image=self.submit_btn, bd=0, relief=FLAT, bg="#334E73", activebackground="#334E73", cursor="hand2")
                    self.submit.place(x=330,y=129)

                    submit_btn_lbl = Label(self.forget_win, text="SUBMIT", bg="#334E73", fg="#4DBBFF", font=("Montserrat", 8))
                    submit_btn_lbl.place(x=338, y=135)

                    self.update_btn = PhotoImage(file="images/update_btn_forgetwin.png")
                    self.update = Button(self.forget_win, command=self.upddate_password, image=self.update_btn, bd=0, relief=FLAT, bg="#334E73", activebackground="#334E73", cursor="hand2")
                    self.update.place(x=209,y=305)


                    # entry 
                    
                    otp_entry = Entry(self.forget_win, relief=FLAT, textvariable=self.var_otp, bd=2, bg="#7794c2", fg="#171836", font=("Montserrat", 12))
                    otp_entry.place(x=209, y=130, width=108, height=27)

                    new_pass_entry = Entry(self.forget_win, relief=FLAT, textvariable=self.var_new_pass, bd=0, bg="#7794c2", fg="#171836", font=("Montserrat", 12))
                    new_pass_entry.place(x=209, y=190, width=190, height=25)

                    confirm_pass_entry = Entry(self.forget_win, relief=FLAT, textvariable=self.var_confirm_pass, bd=0, bg="#7794c2", fg="#171836", font=("Montserrat", 12))
                    confirm_pass_entry.place(x=209, y=247, width=190, height=25)
    
    
    def upddate_password(self):
        if self.var_new_pass.get()=="" or self.var_confirm_pass.get()=="":
            messagebox.showerror("Field Error", "Password should be required", parent=self.forget_win)

        if self.var_new_pass.get()!=self.var_confirm_pass.get():
            messagebox.showerror("Password Don't match", "New password and old password should be same!", parent=self.forget_win)
        
        else:
            con = sqlite3.connect(r"yms.db")
            cur = con.cursor()
            try:
                cur.execute("UPDATE employee SET password=? WHERE eid=?", (self.var_new_pass.get(), self.var_username.get()))
                con.commit()
                messagebox.showinfo("Success", "Your password change successfully. Thank you!", parent=self.forget_win)
                self.forget_win.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Your error due to {es}")


    
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.submit.config(state=NORMAL)
            self.update.config(state=NORMAL)
        
        else:
            messagebox.showerror("Error", "Invalid OTP, try again", parent=self.forget_win)


    def send_email(self, to_):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email_ = email_pass.email_
        pass_ = email_pass.pass_

        s.login(email_, pass_)

        self.otp = int(time.strftime('%H%M%S'))+int(time.strftime('%S'))

        subj = "SMART SHOP  ACCOUNT RECOVER WITH SYSTEM ONE TIME PASSWORD (OTP)"
        msg = f"Dear Sir/Madam.\n\nYour reset OTP is {str(self.otp)}.\n\n With regards,\nexeyexone!"
        msg = 'Subject: {}\n\n{}'.format(subj, msg)

        s.sendmail(email_, to_, msg)
        chk = s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'


    def sing_up(self):

        self.singup_win = Toplevel(self.root)
        self.singup_win.title("Buy System")
        self.singup_win.geometry('598x383+620+220')
        self.singup_win.focus_force()

        self.smart_shop_payment_img = PhotoImage(file="images/smart_shop_payment.png")
        smart_shop_payment_img = Label(self.singup_win, image=self.smart_shop_payment_img, relief=FLAT)
        smart_shop_payment_img.place(x=0, y=0)




    '''def billing(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = billinngClass(self.new_win)

    
    def dashboard(self):
        from dashboard import YMS
        self.new_win= Toplevel(self.root)
        self.new_obj = YMS(self.new_win)'''




if __name__ == "__main__":
    root= Tk()
    obj = loginClass(root)
    root.mainloop()