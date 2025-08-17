import tkinter as tk
from tkinter import messagebox

def Onclick_Submit():
    name=name_textbox.get()
    email=email_textbox.get()
    phone=phone_textbox.get()
    messagebox.showinfo(
        "Captured Data", 
        f"Name: {name}\nEmail: {email}\nPhone: {phone}"
    )

root = tk.Tk()
root.geometry("500x200")
root.title("Student Registration Form")

name_label = tk.Label(root, text="Enter Name")
name_label.pack()

name_textbox = tk.Entry(root)
name_textbox.pack()

email_label = tk.Label(root, text="Enter Email")
email_label.pack()

email_textbox = tk.Entry(root)
email_textbox.pack()

phone_label = tk.Label(root, text="Enter Phone Number")
phone_label.pack()

phone_textbox = tk.Entry(root)
phone_textbox.pack()

submit_button = tk.Button(root, text="Submit", command=Onclick_Submit)
submit_button.pack()

root.mainloop()

