import tkinter as tk
def on_button_click():
    fahrenheit=entry.get()
    celsius =  (int(fahrenheit) - 32)*5/9
    label1 = tk.Label(root, text=f"{entry.get()} F = {int(celsius)} C")
    label1.place(x=90,y=120)
root = tk.Tk()
root.title("Convertor")
root.geometry("300x300")

label = tk.Label(root,text="Enter Fahrenheit")
label.pack(pady=20)
entry=tk.Entry(root)
entry.place(x=90,y=40)

button = tk.Button(root, text="Convert" , command= on_button_click)
button.pack(pady=20)

root.mainloop()