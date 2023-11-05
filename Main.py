from tkinter import *
# from customtkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox  
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

background="#06283D"
framebg="#486982"
framefg= "06283D"

root=Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config()
root.config(bg=background)

background="#06283D"
framebg="#486982"
framefg= "06283D"

file=pathlib.Path('Student_data.xlsx')
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet['A1']='Registration No.'
    sheet['B1']='Full Name'
    sheet['C1']='Date of Birth'
    sheet['D1']='Gender'
    sheet['E1']='Nationality'
    sheet['F1']='Contact Number'
    sheet['G1']='Email Address'
    sheet['H1']='Date of Registration'
    sheet['I1']='Address'
    sheet['J1']="Father's Name"
    sheet['K1']='Parent / Guardian Contact No.'
    sheet['L1']='Previous School/ Instituion'

    file.save('Student_data.xlsx')

#Top_Frames
Label(root,text="Student Registraion", width=10, height=2, bg="#c36464", fg='#fff', font='arial 20 bold').pack(side=TOP, fill=X)

#Search_Bar
Label(root,width=10, height=2, bg="#535659", fg='#fff', font='arial 10').pack(side=TOP, fill=X)

Search=StringVar()
Entry(root,textvariable=Search, width=10, bd=2, font='arial 20').place(x=820, y=70)
imageicon3=PhotoImage(file="Images/search.png")
Srch=Button(root, text="Search", compound=LEFT, image=imageicon3, width=123, bg='#68ddfa', font="arial 13 bold")
Srch.place(x=1060, y=66)

imageicon4=PhotoImage(file="Images/Layer 4.png")
Update_button=Button(root, image=imageicon4, bg="#535659")
Update_button.place(x=110, y=64)

#Registration and Date
Label(root, text="Registration No:", font="arial 13", fg=framebg, bg=background).place(x=30,y=150)
Label(root, text="Date", font="arial 13", fg=framebg, bg=background).place(x=500,y=150)

Registration=StringVar()
Date=StringVar()

reg_entry= Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_entry.place(x=160, y=150)





root.mainloop()