from API import ChatGPT as Gpt


class CommandList:
    def __init__(self, tkinter_instance):
        self.wake_word = "Bobby"
        self.API = Gpt.ChatGPT(tkinter_instance).chat_gpt

        self.regular_command_list = {
            # Browsers
            "Browsers": {
                "Open Firefox": ["firefox"],
                "Open Chrome": ["google-chrome"],
                "Open Opera": ["opera"],
                "Open Bing": ["microsoft-edge"],
                "Open Edge": ["microsoft-edge"],
                "Open Brave": ["brave-browser"],
                "Open Tor": ["tor"],
                "Open DuckDuckGo": ["duckduckgo"],
                "Open Chromium": ["chromium"],
            },

            # Miscellaneous websites
            "Websites": {
                "Open GitHub": ["www.github.com"],
                "Open YouTube": ["www.youtube.com"],
                "Open Twitch": ["www.twitch.tv"],
                "Open Netflix": ["www.netflix.com"],
                "Open Amazon": ["www.amazon.com"],
                "Open Facebook": ["www.facebook.com"],
                "Open Instagram": ["www.instagram.com"],
                "Open Twitter": ["www.twitter.com"],
                "Open Reddit": ["www.reddit.com"],
                "Open Wikipedia": ["www.wikipedia.org"],
                "Open Google": ["www.google.com"],
                "Open Google Maps": ["www.google.com/maps"],
                "Open Google Translate": ["translate.google.com"],
                "Open LinkedIn": ["www.linkedin.com"],
                "Open ChatGPT": ["beta.openai.com"],
                "Open StackOverflow": ["stackoverflow.com"],
                "Open Quora": ["www.quora.com"],
                "Open LeetCode": ["leetcode.com"],
            },

            # University websites
            "University Websites": {
                "Open DTU Learn": ["learn.inside.dtu.dk"],
                "Open DTU Inside": ["inside.dtu.dk"],
                "Open Google Drive": ["drive.google.com"],
                "Open Gmail": ["mail.google.com"],
                "Open Outlook": ["outlook.office.com"],
            },

            # Miscellaneous programs
            "Programs": {
                "Open Spotify": ["spotify"],
                "Open Discord": ["discord"],
                "Open Steam": ["steam"],
                "Open PyCharm": ["pycharm"],
                "Open Clion": ["clion"],
                "Open IntelliJ": ["intellij"],
                "Open VS Code": ["code"],
                "Open Files": ["nautilus"],

                "Open Terminal": ["gnome-terminal"],
                "Open Calculator": ["gnome-calculator"],
                "Open Settings": ["gnome-control-center"],

                "Open Command Prompt": ["cmd"],
                "Open Task Manager": ["gnome-system-monitor"],
                "Open Control Panel": ["gnome-control-center"],
            }
        }

        self.API_command_list = {
            # Browsers
            "API": {
                "GPT Search": self.API
            }
        }
