import speech_recognition as sr
import sounddevice
from datetime import date
from gpiozero import LED
from time import sleep

red = LED(17)
relay1 = LED(14)
relay2 = LED(15)

r = sr.Recognizer()
mic = sr.Microphone()

print("hello")
def voice_recongit():
    while True:
        with mic as source:
            audio = r.listen(source)
        words = r.recognize_google(audio)
        print(words)

while True:
    try:
        voice_recongit()
    except:
        print("word no detection") 
    sleep(0.2)
    if input == ord('q'):
        break
    
