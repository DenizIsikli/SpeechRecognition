import speech_recognition as sr
import subprocess as sp
from TTS import Texttospeech as Tts
import commandlist as cl
from Tkinter import Tkinter as Tk


class Listener:
    def __init__(self):
        # Tkinter configuration
        self.tk = Tk.TkinterWindow()

        # Text to speech configuration
        self.recognizer = sr.Recognizer()

        # Text to speech command
        self.tts_ = Tts.TextToSpeech()
        self.tts = self.tts_.tts

        # Define a dictionary for commands
        self.command_list_class = cl.CommandList()

        self.regular_command_list = self.command_list_class.regular_command_list
        self.API_command_list = self.command_list_class.API_command_list

    @staticmethod
    def has_microphone():
        # Check if the user has a microphone
        try:
            with sr.Microphone():
                return True
        except OSError:
            return False

    def listen(self):
        if not self.has_microphone():
            self.tts("No microphone detected")
            self.tk.update_output_label("No microphone detected")

        microphone_index = 0

        with sr.Microphone(device_index=microphone_index) as source:
            self.tts("Call Bobby to start the program")
            self.tk.update_output_label("Call Bobby to start the program")

            try:
                audio = self.recognizer.listen(source)
                call_assistant = self.recognizer.recognize_google(audio)

                if self.regular_command_list.wake_word in call_assistant:
                    self.process_command()
                    self.tts("Assistant is ready")
                    self.tk.update_output_label("Assistant is ready")
                else:
                    self.tts("Wake word not recognized")
                    self.tk.update_output_label("Wake word not recognized")
            except sr.WaitTimeoutError:
                self.tts("No speech detected")
                self.tk.update_output_label("No speech detected")

    def process_command(self):
        with sr.Microphone() as source:
            self.tts("listening")
            self.tk.update_output_label("listening")

            try:
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)

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
            except sr.WaitTimeoutError:
                self.tts("No speech detected")
                self.tk.update_output_label("No speech detected")
