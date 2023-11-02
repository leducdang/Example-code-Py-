import RPi.GPIO as GPIO
import time

LED1 = 20
LED2 = 21
LED3 = 26
LED4 = 19 

BUTTON1 = 4
BUTTON2 = 17
BUTTON3 = 22
BUTTON4 = 27

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.setup(LED3, GPIO.OUT)
    GPIO.setup(LED4, GPIO.OUT)
    GPIO.setup(BUTTON1, GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON2, GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON3, GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON4, GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setwarnings(False)
    
try:
    setup()
    while True:
        
        if GPIO.input(BUTTON1) == False:
            GPIO.output(LED1, 0)
        else:
            GPIO.output(LED1, 1) 
      #  if BUTTON == 0:
        if GPIO.input(BUTTON2) == False:
            GPIO.output(LED2, 0)
        else:
            GPIO.output(LED2, 1) 
        
        if GPIO.input(BUTTON3) == False:
            GPIO.output(LED3, 0)
        else:
            GPIO.output(LED3, 1) 

        if GPIO.input(BUTTON4) == False:
            GPIO.output(LED4, 0)
        else:
            GPIO.output(LED4, 1) 
            
except KeyboardInterrupt as e:
    print("chuong trinh da hoan thanh")
finally:
    GPIO.cleanup()
    
        