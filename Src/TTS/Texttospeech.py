import time
import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.tts_init = pyttsx3.init()
        self.volume = 0.5

    def tts(self, text, voice: str = "0"):
        engine = self.tts_init
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[int(voice)].id)
        engine.setProperty('volume', float(self.volume))
        engine.say(text)
        engine.runAndWait()
        time.sleep(2)


if __name__ == "__main__":
    tts = TextToSpeech()
    tts.tts("Dennis was made of poop and brain farts", voice="0")
