import tkinter as tk
root = tk.Tk()
root.title("Test App")
root.geometry("250x200")
lbl = tk.Label(root, text="Welcome to Python Tkinter!")
lbl.grid(column=0, row=0)
def on_click():
    lbl.configure(text="Button Clicked")
btn = tk.Button(root, text="Click Here", command = on_click)
btn.grid(column=0, row=1)
root.mainloop()