import tkinter as tk
import time, datetime


class TkinterWindow:
    def __init__(self):
        # Tkinter configuration
        self.tk_ = tk.Tk()

        # Make the window 400x400 and place it in the middle of the screen
        self.tk_.geometry(f"400x400+{int(self.tk_.winfo_screenwidth() / 2 - 200)}+"
                          f"{int(self.tk_.winfo_screenheight() / 2 - 200)}")
        self.tk_.title("Voice Assistant")
        self.tk_.geometry("400x400")
        self.tk_.configure(bg="black")
        self.tk_.configure(cursor="none")
        self.tk_.option_add("*Font", "TkDefaultFont 12")

        # Labels
        self.output_label = tk.Label(self.tk_, text="", bg="black", fg="white")
        self.output_label.grid(row=0, column=0, padx=10, pady=10)

        self.output_timer_label = tk.Label(self.tk_, text="", bg="black", fg="white")
        self.output_timer_label.grid(row=1, column=0, padx=10, pady=10)

        self.input_label = tk.Label(self.tk_, text="", bg="black", fg="white")
        self.input_label.grid(row=2, column=0, padx=10, pady=10)

        self.input_timer_label = tk.Label(self.tk_, text="", bg="black", fg="white")
        self.input_timer_label.grid(row=3, column=0, padx=10, pady=10)

    def update_output_label(self, text):
        if text:
            self.output_label.configure(text=text)
            self.output_timer_label.configure(text=f"Output label updated at: "
                                                   f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
            self.tk_.update()

    def update_input_label(self, text):
        if text:
            self.input_label.configure(text=text)
            self.input_timer_label.configure(text=f"Input label updated at: "
                                                  f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
            self.tk_.update()
