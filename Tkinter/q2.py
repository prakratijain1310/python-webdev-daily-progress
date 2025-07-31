#create a simple window and add image icon

import tkinter as tk
from tkinter import PhotoImage

root=tk.Tk()
icon=PhotoImage(file='image.png')

root.iconphoto(True,icon)
root.geometry("300x300")
root.mainloop()