import tkinter as tk
root = tk.Tk()
root.title("Test App")
lbl = tk.Label(root, text="Label 1")

def on_click():
    lbl.config(text="Button clicked")

lbl.grid(row = 0, column = 0)
lbl2 = tk.Label(root, text="Label 2")
print(lbl.config().keys())
btn = tk.Button(root, text = "Button 1", command = on_click)
btn.grid(row = 1, column = 0)
root.mainloop()


