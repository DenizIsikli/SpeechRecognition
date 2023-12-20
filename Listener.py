import os
import subprocess as sp
from pocketsphinx import LiveSpeech
import commandlist as cl
import pyttsx3
import sounddevice as sd
import webbrowser


class TextToSpeech:
    def __init__(self):
        self.tts_init = pyttsx3.init()
        self.volume = 0.7

    def tts(self, text, voice: str = "0"):
        engine = self.tts_init
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[int(voice)].id)
        engine.setProperty('volume', float(self.volume))
        engine.say(text)
        engine.runAndWait()

    @staticmethod
    def locate_program(program_name: str):
        if not program_name.endswith('.exe'):
            program_name += '.exe'

        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program_name)
            if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
                return exe_file
        return None

    @staticmethod
    def input_devices():
        print(sd.query_devices())


class Listener:
    instance = None

    def __new__(cls, gui_window):
        if cls.instance is None:
            cls.instance = super(Listener, cls).__new__(cls)
        return cls.instance

    def __init__(self, gui_window):
        self.gui_window = gui_window
        self.tts = TextToSpeech().tts
        self.command_list = cl.CommandList().command_list
        self.wake_word = cl.CommandList().wake_word.lower()
        self.speech = LiveSpeech()
        self.terminate = False

    def execute_command(self, command):
        for category_commands in self.command_list.values():
            if command in category_commands:
                command_args = category_commands[command]
                if command_args[0].startswith("http") or command_args[0].startswith("www"):
                    webbrowser.open(command_args[0])
                else:
                    command_path = TextToSpeech.locate_program(command_args[0])
                    if command_path:
                        sp.Popen([command_path])
                    else:
                        print(f"Executable for '{command}' not found.")
                return True
        return False

    def listen(self):
        self.gui_window.update_output_label("Listening...")
        self.tts("Listening...")
        for phrase in self.speech:
            if phrase.is_final():
                recognized_text = str(phrase).lower()
                self.gui_window.update_input_label(recognized_text)

                if recognized_text.startswith(self.wake_word):
                    recognized_text = recognized_text.split(self.wake_word)[1].strip()
                    if recognized_text != "":
                        self.gui_window.update_output_label("Executing command...")
                        self.tts("Executing command...")
                        if not self.execute_command(recognized_text):
                            self.gui_window.update_output_label("I'm sorry, I don't know what you mean.")
                            self.tts("I'm sorry, I don't know what you mean.")
                        self.gui_window.update_output_label("Listening...")
                        self.tts("Listening...")

            if self.terminate:
                break


if __name__ == "__main__":
    tts = TextToSpeech()
    tts.input_devices()
