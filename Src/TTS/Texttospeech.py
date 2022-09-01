import pyttsx3
import time


class TextToSpeech:
    @staticmethod
    def tts(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        time.sleep(2)
