import RPi.GPIO as GPIO
import time 


LED1 = 4
LED2 = 27

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    
try:
    setup()
    while True:
        GPIO.output(LED1,1)
        GPIO.output(LED2,1)
        time.sleep(2)
        GPIO.output(LED1,0)
        GPIO.output(LED2,0)
        time.sleep(2)
except KeyboardInterrupt as e:
    print("ban da hoan thanh xong chuong trinh")
finally:
    GPIO.cleanup()