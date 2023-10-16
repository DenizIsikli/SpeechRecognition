import speech_recognition as sr
import subprocess as sp


class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.command_list = {
            # Browsers
            "Open Firefox": ["firefox"],
            "Open Chrome": ["google-chrome"],
            "Open Opera": ["opera"],
            "Open Bing": ["microsoft-edge"],
            "Open Edge": ["microsoft-edge"],

            # Miscellaneous websites
            "Open GitHub": ["www.github.com"],
            "Open YouTube": ["www.youtube.com"],
            "Open Twitch": ["www.twitch.tv"],
            "Open Netflix": ["www.netflix.com"],
            "Open LinkedIn": ["www.linkedin.com"],
            "Open ChatGPT": ["beta.openai.com"],

            # Miscellaneous programs
            "Open Spotify": ["spotify"],
            "Open Discord": ["discord"],
            "Open Steam": ["steam"],
            "Open PyCharm": ["pycharm"],
            "Open Clion": ["clion"],
            "Open IntelliJ": ["intellij"],
            "Open VS Code": ["code"],
            "Open Files": ["nautilus"],

            # University websites
            "Open DTU Learn": ["learn.inside.dtu.dk"],
            "Open DTU Inside": ["inside.dtu.dk"],
            "Open Google Drive": ["drive.google.com"],
            "Open Gmail": ["mail.google.com"],
            "Open Outlook": ["outlook.office.com"],
        }

    @staticmethod
    def has_microphone():
        # Check if the user has a microphone
        try:
            with sr.Microphone() as _:
                return True
        except OSError:
            return False

    def listen(self):
        if not self.has_microphone():
            print("No microphone found. Please connect a microphone.")
            return

        microphone_index = 0

        with sr.Microphone(device_index=microphone_index) as mic:
            print("Listening...")

            try:
                audio = self.recognizer.listen(mic)
            except sr.WaitTimeoutError:
                print("No speech detected")
                return

            try:
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")

                if command in self.command_list:
                    try:
                        browser = sp.Popen(self.command_list[command])
                        browser.wait()

                    except FileNotFoundError:
                        print(f"Sorry, {command} is not installed on your computer. "
                              f"Please install it or use another browser.")
                else:
                    print("Command not recognized")

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

    def main(self):
        self.listen()


if __name__ == "__main__":
    listener = Listener()
    listener.main()
