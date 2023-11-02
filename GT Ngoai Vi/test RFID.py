import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

LED1=27
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.output(LED1, GPIO.LOW)
reader = SimpleMFRC522()

try:
    while True:
            id, text = reader.read()
            print(id)
            print(type(id))
            print(text)
            sleep(2)

            if id==306286090716:
                print("the hop le")
                GPIO.output(LED1, 1)
                sleep(1)
            else:
                GPIO.output(LED1, 0)
                
except KeyboardInterrupt:
    print("da ket thuc chuong trinh")
    GPIO.cleanup()