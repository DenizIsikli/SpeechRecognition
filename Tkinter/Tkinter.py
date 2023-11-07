import tkinter as tk
from tkinter import messagebox
import datetime
import TTS.Texttospeech


class TkinterWindow:
    def __init__(self):
        self.text_to_speech = TTS.Texttospeech.TextToSpeech()

        self.tk_ = tk.Tk()

        # Make the window 400x400 and place it in the middle of the screen
        self.tk_.geometry(f"500x500+{int(self.tk_.winfo_screenwidth() / 2 - 200)}+"
                          f"{int(self.tk_.winfo_screenheight() / 2 - 200)}")
        self.tk_.title("Voice Assistant")
        self.tk_.configure(bg="white")
        self.tk_.option_add("*Font", "Courier 12")
        # self.tk_.overrideredirect(True)

        # Create a frame to center the content
        content_frame = tk.Frame(self.tk_)
        content_frame.pack(expand=True)

        # Labels
        self.output_label = tk.Label(content_frame, text="", bg="white", fg="black")
        self.output_label.pack(side=tk.TOP, padx=10, pady=10)

        self.output_timer_label = tk.Label(content_frame, text="", bg="white", fg="black")
        self.output_timer_label.pack(side=tk.TOP, padx=10, pady=10)
        self.output_timer_label.config(font=("Courier", 8))

        self.input_label = tk.Label(content_frame, text="", bg="white", fg="black")
        self.input_label.pack(side=tk.TOP, padx=10, pady=10)

        self.input_timer_label = tk.Label(content_frame, text="", bg="white", fg="black")
        self.input_timer_label.pack(side=tk.TOP, padx=10, pady=10)
        self.input_timer_label.config(font=("Courier", 8))

        # Dropdown menu (Voice options)
        self.selected_voice = tk.StringVar(self.tk_)
        self.selected_voice.set("0")

        self.voice_label = tk.Label(content_frame, text="Select Voice")
        self.voice_label.pack(side=tk.TOP, padx=10, pady=10)

        # 0: Male | 1: Female
        voice_options = ("0", "1")

        self.voice_dropdown = tk.OptionMenu(content_frame, self.selected_voice, *voice_options)
        self.voice_dropdown.pack(side=tk.TOP, padx=10, pady=10)

        # Attach a callback to the variable to apply the selected voice
        self.selected_voice.trace("w", self.apply_selected_voice)

        # Bind closing event to on_closing method
        self.tk_.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if messagebox.askokcancel("Exit", "Do you want to exit the application?"):
            self.tk_.destroy()

    def apply_selected_voice(self, *_):
        voice_index = self.selected_voice.get()
        default_text = ""

        if voice_index == "0":
            default_text = "Male"
        elif voice_index == "1":
            default_text = "female"

        self.text_to_speech.tts(text=default_text, voice=voice_index)

    def update_output_label(self, text):
        if text:
            self.output_label.configure(text=text)
            self.output_timer_label.configure(text=f'Output label updated at: '
                                                   f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            self.tk_.update()

    def update_input_label(self, text):
        if text:
            self.input_label.configure(text=text)
            self.input_timer_label.configure(text=f'Input label updated at: '
                                                  f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            self.tk_.update()

    def run(self):
        self.tk_.mainloop()
