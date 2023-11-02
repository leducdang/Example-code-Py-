import RPi.GPIO as GPIO
import time

LED_PWM = 13

try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PWM, GPIO.OUT)
    pwm = GPIO.PWM(LED_PWM , 100)
    pwm.start(0)
    
    while True:
        pwm.ChangeDutyCycle(0)
        time.sleep(2)
        pwm.ChangeDutyCycle(25)
        time.sleep(2)
        pwm.ChangeDutyCycle(0)
        pwm.stop()
        time.sleep(2)
        pwm.start(0)
    
except KeyboardInterrupt :
    print("da tat chuong trinh")
    pwm.stop()
    GPIO.cleanup()