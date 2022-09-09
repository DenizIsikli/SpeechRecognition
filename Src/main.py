import speech_recognition as sr
import subprocess as sp
import pyttsx3
import commandlist as cl
import Tkinter as Tk
import time


class Listener(Tk):
    def __init__(self):
        # Base Class
        self.bc = super().__init__()

        self.recognizer = sr.Recognizer()

        # Define a dictionary for commands
        self.command_list_ = cl.CommandList()
        self.command_list = self.command_list_.command_list

    @staticmethod
    def has_microphone():
        # Check if the user has a microphone
        try:
            with sr.Microphone() as _:
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
            self.tts("No microphone found. Please connect a microphone.")
            self.bc.update_output_label("No microphone found. Please connect a microphone.")
            self.bc.clear_label()

        microphone_index = 0

        with sr.Microphone(device_index=microphone_index) as mic:
            self.tts("Listening...")
            self.bc.update_output_label("Listening...")
            self.bc.clear_label()

            try:
                audio = self.recognizer.listen(mic)
            except sr.WaitTimeoutError:
                self.tts("No speech detected")
                self.bc.update_output_label("No speech detected")
                self.bc.clear_label()

            try:
                command = self.recognizer.recognize_google(audio)
                self.tts(f"Recognized: {command}")
                self.bc.update_input_label(f"{command}")
                self.bc.clear_label()

                if command in self.command_list:
                    try:
                        self.tts(f"Opening {command}")
                        self.bc.update_output_label(f"Opening {command}")
                        self.bc.clear_label()

                        browser = sp.Popen(self.command_list[command])
                        browser.wait()
                    except FileNotFoundError:
                        self.tts(f"Sorry, {command} is not installed on your computer.")
                        self.bc.update_output_label(f"Sorry, {command} is not installed on your computer.")
                        self.bc.clear_label()
                else:
                    self.tts("Command not recognized")
                    self.bc.update_output_label("Command not recognized")

            except sr.UnknownValueError:
                self.tts("Could not understand audio")
                self.bc.update_output_label("Could not understand audio")
            except sr.RequestError as e:
                self.tts(f"Could not request results; {e}")
                self.bc.update_output_label(f"Could not request results; {e}")


if __name__ == "__main":
    listener = Listener()
    listener.listen()
