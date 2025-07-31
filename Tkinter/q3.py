'''import tkinter as tk

root = tk.Tk()
root.geometry('200x200')

label1=tk.Label(root,text='label1',bg='lavender')
label1.pack(fill=tk.BOTH,expand=True)
label2=tk.Label(root,text='label2',bg='pink')
label2.pack(fill=tk.BOTH,expand=True)

root.mainloop()
'''
'''import tkinter as tk

root = tk.Tk()
root.geometry('200x200')

label1=tk.Label(root,text='label1',bg='lavender')
label1.grid(row=0, column=0)
label2=tk.Label(root,text='label2',bg='pink')
label2.grid(row=1, column=1)

root.mainloop()'''

import tkinter as tk

root = tk.Tk()
root.geometry('200x200')

label1=tk.Label(root,text='label1',bg='lavender')
label1.place(x=0, y=0)
label2=tk.Label(root,text='label2',bg='pink')
label2.place(x=60, y=120)

root.mainloop()