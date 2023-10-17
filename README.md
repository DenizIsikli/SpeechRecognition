# Still does not work because Python 3.12 still has issue installing dependencies due to it's recent release

# Voice Assistant
A simple voice assistant built in Python using Speech Recognition, subprocess, and Pyttsx3.
Table of Contents

- Description
- Features
- Requirements
- Installation
- Usage
- Project Structure
- Contributing
- License

## Description
This voice assistant is a Python application that listens to voice commands and performs tasks based on the recognized commands. It uses the Speech Recognition library to capture audio input, processes the audio to extract recognized text, and then executes corresponding commands. The recognized commands include opening web browsers, websites, and various programs.

## Features
- Open popular web browsers like Firefox, Chrome, and more.
- Access various websites such as GitHub, YouTube, and LinkedIn.
- Launch programs like Spotify, Discord, and PyCharm.
- Recognizes university websites and email services.

## Requirements
- Python 3.x
- SpeechRecognition
- pyttsx3

## Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/voice-assistant.git
```

Install the required libraries:

```bash
    pip install SpeechRecognition pyttsx3
```

## Usage
Run the main script:

```bash
    python main.py
```
Ensure your microphone is connected.
Start giving voice commands.

## Project Structure
- listener.py: Contains the main functionality of the voice assistant.
- tkinter.py: Defines the graphical user interface for displaying feedback.
- commandlist.py: Provides a list of recognized commands and their corresponding actions.
- main.py: Entry point for starting the voice assistant.

## License
This project is licensed under the MIT License.
