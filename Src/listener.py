import speech_recognition as sr
import subprocess as sp
import pyttsx3
import commandlist as cl
import Tkinter as tk
import time


class Listener():
    def __init__(self):
        self.tk_ = tk.TkinterWindow()
        self.recognizer = sr.Recognizer()

        # Define a dictionary for commands
        self.command_list_ = cl.CommandList()
        self.command_list = self.command_list_.command_list

    @staticmethod
    def has_microphone():
        # Check if the user has a microphone
        try:
            with sr.Microphone():
                return True
        except OSError:
            return False

    @staticmethod
    def tts(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        time.sleep(2)

    def listen(self):
        if not self.has_microphone():
            self.tts("No microphone detected")
            self.tk_.update_output_label("No microphone detected")
            self.tk_.clear_label()

        microphone_index = 0

        with sr.Microphone(device_index=microphone_index) as source:
            self.tts("Call Bobby to start the program")
            self.tk_.update_output_label("Call Bobby to start the program")
            self.tk_.clear_label()

            try:
                audio = self.recognizer.listen(source)
                call_assistant = self.recognizer.recognize_google(audio)

                if self.command_list_.wake_word in call_assistant:
                    self.process_command()
                    self.tts("Assistant is ready")
                    self.tk_.update_output_label("Assistant is ready")
                    self.tk_.clear_label()
                else:
                    self.tts("Wake word not recognized")
                    self.tk_.update_output_label("Wake word not recognized")
                    self.tk_.clear_label()
            except sr.WaitTimeoutError:
                self.tts("No speech detected")
                self.tk_.update_output_label("No speech detected")
                self.tk_.clear_label()

    def process_command(self):
        with sr.Microphone() as source:
            self.tts("listening")
            self.tk_.update_output_label("listening")
            self.tk_.clear_label()

            try:
                audio = self.recognizer.listen(source)
                command= self.recognizer.recognize_google(audio)

                if command in self.command_list:
                    sp.Popen(self.command_list[command])
                    self.tts("Executing command")
                    self.tk_.update_output_label("Executing command")
                    self.tk_.clear_label()
                else:
                    self.tts("Command not recognized")
                    self.tk_.update_output_label("Command not recognized")
                    self.tk_.clear_label()
            except sr.WaitTimeoutError:
                self.tts("No speech detected")
                self.tk_.update_output_label("No speech detected")
                self.tk_.clear_label()
