import aiohttp
from TTS import Texttospeech as Tts


class ChatGPT:
    def __init__(self, tkinter_instance):
        self.tk = tkinter_instance

        # RapidAPI Link
        self.API = "https://simple-chatgpt-api.p.rapidapi.com/ask"

        # Text to speech command
        self.tts_ = Tts.TextToSpeech()
        self.tts = self.tts_.tts

    async def chat_gpt(self, *, command: str = None):
        if command is None:
            self.tts("Please provide text when using the command")
            self.tk.update_output_label("Please provide text when using the command")

        try:
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "2ba10896fdmsh6eb24b198a7b520p1fef74jsneb8afa07df45",
                "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
            }

            payload = {"question": command}

            async with aiohttp.ClientSession() as session:
                async with session.post(self.API, json=payload, headers=headers) as response:
                    response.raise_for_status()  # Raise an exception if the request was not successful
                    response_data = await response.json()

                    ai_response = response_data.get('answer', 'No response from the AI')

                    self.tts(ai_response)
                    self.tk.update_output_label(ai_response)

        except Exception as e:
            self.tts(f"An error occurred: {e}")
            self.tk.update_output_label(f"An error occurred: {e}")
