import RPi.GPIO as GPIO
import time

LED_PWM = 13

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PWM, GPIO.OUT)
    pwm = GPIO.PWM(LED_PWM , 100) # SET CHAN pwm duoc su dung co 100 muc
    pwm.start(0)   #bat dau chay o muc 0
    while True:
        for x in range(0,100):
            pwm.ChangeDutyCycle(x)
            time.sleep(0.5)
            print(x)
        
        time.sleep(2 )
        
except KeyboardInterrupt :
    print("da tat chuong trinh")
    
    GPIO.cleanup()
        
    