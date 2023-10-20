from Tkinter import Tkinter as Tk
from Listener import Listener as Ls

if __name__ == "__main__":
    tk = Tk.TkinterWindow()
    ls = Ls.Listener()

    tk.run()
    ls.listen()
