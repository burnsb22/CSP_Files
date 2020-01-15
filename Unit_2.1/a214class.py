import tkinter as tk
import string

root = tk.Tk()

def login():
    if password_validation(password_entry.get()):
        print('You have entered a valid Password!')
    else:
        print("Invalid Password attempt, please retry.")




def password_validation(entered_password):
    if len(entered_password) <= 7:
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
submit.pack()

signup_btn = tk.Button(root, text='Sign up', command=pass)
signup_btn.pack()

root.mainloop()