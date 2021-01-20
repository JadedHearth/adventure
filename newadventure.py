import tkinter as tk
from PIL import Image, ImageTk
from time import sleep

cmds = "Commands: (note - subject to (constant) change)\n'move' - lets you move from one town to another.\n'location' - tells you your current location.\n'visit' - lets you move to a building.\n'chat' - lets you talk to NPCs if in a building that isnt a shop or a job.\n'shop' - opens the shop if it exists."

class MainApplication():
    def __init__(self, parent):
        self.loadmap = Image.open("map.png")
        self.loadmap = self.loadmap.resize((512, 376), Image.ANTIALIAS)
        self.rendermap = ImageTk.PhotoImage(self.loadmap)
        self.widget_creation()
        self.grid_resize()

    def widget_creation(self):
        # Creating
        self.content = tk.Frame(root, padx = 6, pady = 6, bg = "gray15")
        self.terminal = tk.Frame(self.content, borderwidth = 5, relief = "sunken", width = 200, height = 100, bg = "orange")
        self.cmdhelp = tk.Label(self.content, text = cmds, fg = "white", bg = "gray20")
        self.map = tk.Label(self.content, image = self.rendermap, bg = "gray20")
        self.map.image = self.rendermap
        self.entry = tk.Entry(self.terminal, bg = "dark orange")

        # Tells where to put them
        self.content.grid(column = 0, row = 0, sticky = ("NSEW"))
        self.terminal.grid(column = 1, row = 0, rowspan = 2, sticky = ("NSEW"))
        self.cmdhelp.grid(column = 0, row = 0, sticky = ("N"), padx = 5)
        self.map.grid(column = 0, row = 1, padx = 6, pady = 6)
        self.entry.pack(side = "bottom", fill = "x")

        # Event creation
        self.entry.bind("<Return>",  self.terminal_enter) # Pressing the enter key
        root.bind("<Configure>", self.configure) # Resizing the window

    def grid_resize(self):
        # Grid config
        self.content.columnconfigure(0, weight = 1, minsize = 524)
        self.content.columnconfigure(1, weight = 1, minsize = 300)
        self.content.rowconfigure(0, weight = 1)
        self.content.rowconfigure(1, weight = 1)

    def configure(self, event):
        self.loadmap = self.loadmap.resize((self.map.winfo_width(), self.map.winfo_height()), Image.ANTIALIAS)
        self.map = tk.Label(self.content, image = self.rendermap, bg = "gray20")
        self.map.image = self.rendermap
        self.map.grid(column = 0, row = 1, padx = 6, pady = 6)

    def terminal_enter(self, event):
        print("test:")
        print(test)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Adventure")
    root.geometry("1000x600")
    root.minsize(836, 600)
    MainApplication(root)
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.mainloop()
