import tkinter as tk
root = tk.Tk()
root.title("Simple App")
def add_to_list():
    text =  entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0,tk.END)


frame = tk.Frame(root)
frame.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

entry.bind("<Return>", lambda e: add_to_list())

entry_btn = tk.Button(frame, text="Add", command = add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0)

root.mainloop()


