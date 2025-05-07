import playsound
from utils import speak

def play_last_message():
    speak("Playing your last message.")
    playsound.playsound("recordings/sample_message.wav")
