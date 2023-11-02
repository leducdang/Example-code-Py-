import RPi.GPIO as GPIO
import time

LED1 = 20

sensor = 6


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(sensor, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    
    
try:
    setup()
    while True:
        
        if GPIO.input(sensor) == False:
            print("co vat")
            GPIO.output(LED1, 0)
            time.sleep(0.1)
        else:
            GPIO.output(LED1, 1)  
            
except KeyboardInterrupt as e:
    print("chuong trinh da hoan thanh")
finally:
    GPIO.cleanup()
    
        