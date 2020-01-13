import tkinter as tk

root = tk.Tk()

root.wm_geometry("800x600")

root.wm_title("Login Practice")

username_lbl = tk.Label(root, text="Username")
username_lbl.grid()


root.mainloop()