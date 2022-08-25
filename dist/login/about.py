from email import message
from email.mime import image
from re import L
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext
from turtle import color, left, onclick
import sqlite3
import create_db 


class aboutClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1000x582+255+130')
        self.root.config(bg="#10213b")
        self.root.focus_force()
        self.root.iconbitmap('images/icon.ico')
        self.root.title("Your's Management System | Developed by Tahamidur Taief")


        self.about_page_img = PhotoImage(file="images/about_page.png")
        about_page_img = Label(self.root, image=self.about_page_img, relief=FLAT)
        about_page_img.place(x=0, y=0)


if __name__ == "__main__":
    root= Tk()
    obj = aboutClass(root)
    root.mainloop()