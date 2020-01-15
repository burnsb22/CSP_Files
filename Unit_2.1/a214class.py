import tkinter as tk
import string
from passlib.hash import pbkdf2_sha256

root = tk.Tk()

users = {}

def login():
    pass

def sign_up():
    if password_validation(password_entry.get()):
        result_lbl.config(text='You have entered a valid password!')
    else:
        result_lbl.config(text="Invalid Password attempt, please retry.")
    users[username_entry.get()] = password_entry.get()  

def password_validation(entered_password):
    if len(entered_password) < 8:
        return False
    elif not any(char.isupper() for char in entered_password):
        return False
    elif not any(char.islower() for char in entered_password):
        return False  
    elif not any(char.isdigit() for char in entered_password):
        return False
    elif not any(char in string.punctuation for char in entered_password):
        return False
    else:
        return True  

def encrypting_passwords():
    hash = pbkdf2_sha256.hash()

root.wm_geometry("800x600")

root.wm_title("Login Practice")


username_lbl = tk.Label(root, text="Username")
username_lbl.pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_lbl = tk.Label(root, text="Password")
password_lbl.pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

submit = tk.Button(root, text='Login', command=login)
submit.pack(pady=10)

signup_btn = tk.Button(root, text='Sign up', command=sign_up)
signup_btn.pack(pady=10)

result_lbl = tk.Label(root, text='Result Label')
result_lbl.pack(pady=20)

root.mainloop()