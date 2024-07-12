import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter import messagebox as ms
import os

global fn
fn = ""

root = tk.Tk()
root.configure(background="brown")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("_Land Classification On Satellite Images_")

# For background Image
image2 = Image.open('I2.jpg')
image2 = image2.resize((1600,1000), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

label_l1 = tk.Label(root, text="_Land Classification On Satellite Images_",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="white", width=60, height=1)
label_l1.place(x=0, y=0)

def reg():
    os.system("python registration.py")

def log():
    os.system("python login.py")

def window():
    root.destroy()

button1 = tk.Button(root, text="Login", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=160)

button2 = tk.Button(root, text="Register", command=reg, width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button2.place(x=100, y=240)

button3 = tk.Button(root, text="Exit", command=window, width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=100, y=330)

root.mainloop()
