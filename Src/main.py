from Tkinter import Tkinter as Tk
from Listener import Listener as Ls
import threading

if __name__ == "__main__":
    tk = Tk.TkinterWindow()
    ls = Ls.Listener(tk)

    # Create a thread to run the listener
    listener_thread = threading.Thread(target=ls.listen)

    listener_thread.start()

    tk.run()
