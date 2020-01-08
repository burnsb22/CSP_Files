##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x100")
root.wm_title('Authorization')

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()

def callback():
    print("click!")

btn_login = Button(frame_login, text="Login", command=callback)
btn_login.pack()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login,text="Password:")
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

root.mainloop()