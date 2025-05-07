import sounddevice as sd
import scipy.io.wavfile as wav
from utils import speak

def send_voice_message():
    speak("Please record your message after the beep.")
    fs = 44100
    duration = 5
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    wav.write("recordings/sample_message.wav", fs, recording)
    speak("Your message has been recorded.")
