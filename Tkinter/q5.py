#to add button
import tkinter as tk
root=tk.Tk()
root.geometry('300x200')

frame_top=tk.Frame(root)
frame_top.pack(side=tk.TOP,pady=10)
frame_bottom=tk.Frame(root)
frame_bottom.pack(side=tk.TOP,pady=10)

label=tk.Label(frame_top,text='hello, tkinter!')
label.pack()

button=tk.Button(frame_bottom,text='Click Me',command=lambda:label.config(text='Button Clicked'))
button.pack()

root.mainloop()

import tkinter as tk
def on_button_click():
    label.config(text="Button Clicked")
    
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x300")

label = tk.Label(root,text="Hello , Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me" , command= on_button_click)
button.pack(pady=20)

root.mainloop()
'''
import tkinter as tk
def on_button_click():
    label.config(text="Button Clicked")
    
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x300")

label = tk.Label(root,text="Hello , Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me" , command= on_button_click)
button.pack(pady=20)

root.mainloop()'''