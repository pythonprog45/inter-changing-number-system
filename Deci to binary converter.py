#pre requisites:- 1) install tkinter

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x100")
root.title("Decimal number to binary")

warn = tk.Label(root, text = "Warn: You might get the answer in list form")

n_label = tk.Label(root, text = "Enter the number: ")
n_enter = tk.Entry(root, width = 27)

def click():
    num_get = int(n_enter.get())
    bin_num = str(bin(num_get))
    d_num_list = []
    o_num_list = []
    for i in bin_num:
        d_num_list.append(i)
    o_num_list.append(d_num_list[2:])
    num = ""
    for na in o_num_list:
        num = num + str(na)

    messagebox.showinfo(message = f"binary number of {num_get} is {num}")
    n_enter.focus_set()
    n_enter.delete(0, tk.END)



enter = tk.Button(root, text = " Calculate! ", command = click)

n_label.grid(row = 2, column = 1, pady = 10)
n_enter.grid(row = 2, column = 2)

warn.grid(row = 2 , column = 3)
enter.grid(row = 3, column = 2)

root.mainloop()

