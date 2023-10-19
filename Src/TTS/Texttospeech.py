import time
import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.tts_init = pyttsx3.init()

    def tts(self, text):
        engine = self.tts_init
        engine.say(text)
        engine.runAndWait()
        time.sleep(2)

    @staticmethod
    def list_voices_from_registry(voice: int = 0):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[voice].id)

        engine.runAndWait()


if __name__ == "__main__":
    tts = TextToSpeech()
    tts.list_voices_from_registry(voice=0)
