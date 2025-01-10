#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
# import tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")

# create empty frame (new window for components in root)
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)

# Activate the grid in our new frame
frame_login.grid(row="0", column="0", sticky="news")
frame_auth.grid(row="0", column="0", sticky="news")

def login():
    frame_auth.tkraise()



# widgets for frame_login

#username Label
lbl_username = tk.Label(frame_login, text="Username", fg="red", font="Times 14")
lbl_username.pack(padx=50)

# Text box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

#password Label
lbl_password = tk.Label(frame_login, text="Password", fg="Blue", font="Times 14")
lbl_password.pack(padx=50)

# Text box for password
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack()

# login button
button_login = tk.Button(frame_login, text="Login", command=login)
button_login.pack(pady=10)

#password Label
lbl_authorized = tk.Label(frame_auth, text="Authorization Screen", font="Times 14")
lbl_authorized.pack(padx=50)

frame_login.tkraise()
root.mainloop()