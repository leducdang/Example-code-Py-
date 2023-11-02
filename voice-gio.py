import speech_recognition as sr
import sounddevice
from datetime import date
from gpiozero import LED
from time import sleep

den1 = LED(17)
den2 = LED(14)
den3 = LED(15)

r = sr.Recognizer()
mic = sr.Microphone()

print("hello")
def voice_recongit():
    while True:
        with mic as source:
            audio = r.listen(source)
        words = r.recognize_google(audio)
        print(words)

        if words == "today":
            print(date.today())

        if words == "turn on one":
            print(" den 1 bat")
            den1.on()

        if words == "turn off one":
            print(" den 1 tat")
            den1.off()

        if words == "turn on two":
            print(" den 2 bat")
            den2.on()

        if words == "turn off two":
            print(" den 2 tat")
            den2.off()

        if words == "turn on three":
            print(" den 3 bat")
            den3.on()

        if words == "turn off three":
            print(" den 3 tat")
            den3.off()

        if words == "goodbye":
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("Goodbye")
            break
while True:
    try:
        voice_recongit()
    except:
        print("word un recongition") 
    sleep(0.1)
        
    
