from tkinter import *
from tkinter import ttk

root = Tk()

# Creation of some widgets
content = ttk.Frame(root, padding = (3,3,12,12))
frame = ttk.Frame(content, borderwidth = 5, relief = "sunken", width = 200, height = 100)
namelbl = ttk.Label(content, text = "Commands:")
name = ttk.Entry(content)
ok = ttk.Button(content, text = "Okay")
cancel = ttk.Button(content, text = "Cancel")

# Location of widgets
content.grid(column = 0, row = 0, sticky = (N, S, E, W))
frame.grid(column = 0, row = 0, columnspan = 3, rowspan = 1, sticky = (N, S, E, W))
namelbl.grid(column = 3, row = 0, columnspan = 2, sticky = (N, W), padx = 5)
name.grid(column = 3, row = 1, columnspan = 2, sticky = (N, E, W), pady = 5, padx = 5)
ok.grid(column = 3, row = 3)
cancel.grid(column = 4, row = 3)

# Tells how to resize
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
content.columnconfigure(0, weight = 3)
content.columnconfigure(1, weight = 3)
content.columnconfigure(2, weight = 3)
content.columnconfigure(3, weight = 1)
content.columnconfigure(4, weight = 1)
content.rowconfigure(0, weight = 1)
content.rowconfigure(1, weight = 1)

# Creates all of the set widgets
root.mainloop()
