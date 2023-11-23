from tkinter import *
from tkinter import messagebox
import mysql.connector


background='#06283D'
framebg='EDEDED'
framefg='#06283D'

root=Tk()
root.title('Login System')
root.geometry('1250x700+210+100')
root.config(bg=background)
root.resizable(False,False)


#favicon
fav_icon=PhotoImage(file='Images/favicon.png')
root.iconphoto(False, fav_icon)

#Background Image

frame=Frame(root,bg='red')
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="Images/LOGIN.PNG")
Label(frame, image=backgroundimage).pack()


root.mainloop()