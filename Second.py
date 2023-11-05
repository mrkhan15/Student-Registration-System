from customtkinter import *
from customtkinter.windows import CTk
import tkinter as tk
import pathlib
from datetime import date
from tkinter import filedialog, PhotoImage, messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
from customtkinter import CTkFont

app = CTk()
app.title("Student Registration System")
# set_appearance_mode("dark")
app.geometry("500x400")

#Save Data to Exel file
file=pathlib.Path('Student_data3.xlsx')
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

    file.save('Student_data3.xlsx')



# Adjust family and size as needed
font = CTkFont(family='Roboto', size=15, weight='bold')  

#Top_Frames 
label = CTkLabel(app, text="STUDENT REGISTRATION", font=font, width=2, height=50, fg_color='#c0c9fe')
label.pack(fill=X)

# main_view
main_view = CTkFrame(master=app,  corner_radius=0)
main_view.pack(side="top")


# Create a button to trigger the search action
def perform_search():
    query = search_entry.get()
    # Add your search logic here
    print(f"Performing search for: {query}")

# Search bar
search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
search_container.pack(fill="x")

search_entry = CTkEntry(master=search_container, width=305, placeholder_text="Search", border_color="#c0c9fe", border_width=2)
search_entry.pack(side="left")

search_button_image = PhotoImage(file="search_icon.png")
search_button = CTkButton(search_container, image=search_button_image, text=" ", fg_color='#c0c9fe', width=20, height=20, command=perform_search)
search_button.pack(side="left")

# Rest of your code...

app.mainloop()
