from tkinter import *
import socket

def check_connection():
    try:
        # Try connecting to Google DNS
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False

root = Tk()

if check_connection():
    Label(root, text="Connected to tYour om anahajgoodcoding sckills me dcoing coding aaah coding he Internet").pack()
else:
    Label(root, text="No Internet Connection").pack()
# Init
root = Tk()

# Var
PlaceID = None

# Compound Interest
TitlePg1 = Label(root, font="Arial", compound=CENTER, text=f"Weather in {PlaceID}.")
TitlePg1.pack()

root.mainloop()