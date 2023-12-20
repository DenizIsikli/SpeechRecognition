import speech_recognition as sr
import subprocess as sp
from TTS import Texttospeech as Tts
import commandlist as cl


class Listener:
    instance = None

    def __new__(cls, tkinter_instance):
        if cls.instance is None:
            cls.instance = super(Listener, cls).__new__(cls)
        return cls.instance

    def __init__(self, tkinter_instance):
        self.tk = tkinter_instance

        # Text to speech configuration
        self.recognizer = sr.Recognizer()

        # Text to speech command
        self.tts_ = Tts.TextToSpeech()
        self.tts = self.tts_.tts

        # Define a dictionary for commands
        self.command_list_class = cl.CommandList(tkinter_instance)

        self.wake_word = self.command_list_class.wake_word
        self.regular_command_list = self.command_list_class.regular_command_list
        self.API_command_list = self.command_list_class.API_command_list

        self.microphone_index = 2
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

    def recognize_speech(self, audio):
        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return f"Speech recognition error: {e}"

    def process_command(self, command):
        self.tk.update_output_label("listening")
        self.tts("listening")

        if command in self.regular_command_list:
            sp.Popen(self.regular_command_list[command])
            self.tk.update_input_label(command)
            self.tk.update_output_label("Executing command")
            self.tts("Executing command")
        elif command in self.API_command_list:
            self.API_command_list[command]()
            self.tk.update_input_label(command)
            self.tk.update_output_label("Executing command")
            self.tts("Executing command")
        else:
            self.tk.update_output_label("Command not recognized")
            self.tts("Command not recognized")

    def listen(self):
        while not self.terminate:
            if not self.has_microphone():
                self.tk.update_output_label("No microphone detected")
                self.tts("No microphone detected")

            with sr.Microphone(device_index=self.microphone_index) as source:
                self.tk.update_output_label("Call Bobby to start the program")
                self.tts("Call Bobby to start the program")

                try:
                    audio = self.recognizer.listen(source)

                    call_assistant = self.recognize_speech(audio)

                    self.process_command(call_assistant)

                    # if self.wake_word in call_assistant:
                    #     self.process_command(call_assistant)
                    #     self.tk.update_input_label(call_assistant)
                    #     self.tk.update_output_label("Assistant is ready")
                    #     self.tts("Assistant is ready")
                    # else:
                    #     self.tk.update_output_label("Wake word not recognized")
                    #     self.tts("Wake word not recognized")
                except sr.WaitTimeoutError:
                    self.tk.update_output_label("No speech detected")
                    self.tts("No speech detected")

            if call_assistant == "Terminate":
                self.terminate = True
                self.tts("Terminating program")


if __name__ == "__main__":
    instance = None
    ls = Listener(instance)
    ls.list_microphone()