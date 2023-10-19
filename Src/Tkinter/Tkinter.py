import tkinter as tk
import datetime

import TTS.Texttospeech


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

        # Dropdown menu (Voice options)
        self.selected_voice = tk.StringVar(self.tk_)
        self.selected_voice.set("0")

        self.voice_label = tk.Label(self.tk_, text="Select Voice")
        self.voice_label.grid(row=4, column=0, padx=10, pady=10)

        voice_options = ("0", "1")

        self.voice_dropdown = tk.OptionMenu(self.tk_, self.selected_voice, *voice_options)
        self.voice_dropdown.grid(row=4, column=1, padx=10, pady=10)

        # Attach a callback to the variable to apply the selected voice
        self.selected_voice.trace("w", self.apply_selected_voice)

    def apply_selected_voice(self):
        voice_index = self.selected_voice.get()

        text_to_speech = TTS.Texttospeech.TextToSpeech()
        text_to_speech.list_voices_from_registry(voice=int(voice_index))

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
