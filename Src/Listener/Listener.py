import time
import speech_recognition as sr
import subprocess as sp
from TTS import Texttospeech as Tts
import commandlist as cl
from Tkinter import Tkinter as Tk


class Listener:
    instance = None
    tk = Tk.TkinterWindow()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Listener, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # Text to speech configuration
        self.recognizer = sr.Recognizer()

        # Text to speech command
        self.tts_ = Tts.TextToSpeech()
        self.tts = self.tts_.tts

        # Define a dictionary for commands
        self.command_list_class = cl.CommandList()

        self.wake_word = self.command_list_class.wake_word
        self.regular_command_list = self.command_list_class.regular_command_list
        self.API_command_list = self.command_list_class.API_command_list

        self.microphone_index = 1
        self.terminate = False

    @staticmethod
    def has_microphone():
        # Check if the user has a microphone
        try:
            with sr.Microphone():
                return True
        except OSError:
            return False

    @staticmethod
    def list_microphone():
        mic_list = sr.Microphone.list_microphone_names()

        for i, microphone in enumerate(mic_list):
            print(f"Microphone: {i} - {microphone}")

    def listen(self):
        while not self.terminate:
            if not self.has_microphone():
                self.tts("No microphone detected")
                self.tk.update_output_label("No microphone detected")

            with sr.Microphone(device_index=self.microphone_index) as source:
                time.sleep(3)
                self.tts("Call Bobby to start the program")
                self.tk.update_output_label("Call Bobby to start the program")

                try:
                    audio = self.recognizer.listen(source)
                    call_assistant = self.recognizer.recognize_sphinx(audio)

                    if self.wake_word in call_assistant:
                        self.process_command(call_assistant)
                        self.tts("Assistant is ready")
                        self.tk.update_output_label("Assistant is ready")
                    else:
                        self.tts("Wake word not recognized")
                        self.tk.update_output_label("Wake word not recognized")
                except sr.WaitTimeoutError:
                    self.tts("No speech detected")
                    self.tk.update_output_label("No speech detected")

            if call_assistant == "Terminate":
                self.terminate = True

    def process_command(self, command):
        self.tts("listening")
        self.tk.update_output_label("listening")

        if command in self.regular_command_list:
            sp.Popen(self.regular_command_list[command])
            self.tts("Executing command")
            self.tk.update_input_label(command)
            self.tk.update_output_label("Executing command")
        elif command in self.API_command_list:
            self.API_command_list[command]()
            self.tts("Executing command")
            self.tk.update_input_label(command)
            self.tk.update_output_label("Executing command")
        else:
            self.tts("Command not recognized")
            self.tk.update_output_label("Command not recognized")


if __name__ == "__main__":
    listener = Listener()
    listener.list_microphone()
