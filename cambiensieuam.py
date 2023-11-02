#note: truoc khi chay chan echo can qua cau phan ap de giam tu 5v->3.3v


import RPi.GPIO as GPIO
import time

time_start = 0
time_end = 0
long_time = 0
TRIG = 23
ECHO = 24

def setup_GPIO():
    GPIO.setmode(GPIO.BCM)  #SET CHE DO GHI CHO GPIO
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setwarnings(False)
    
try:
    setup_GPIO()
    while True:        
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG, 0)
        while GPIO.input(ECHO) == 0:
            time_start = float(time.time())                    
        
        while GPIO.input(ECHO) == 1:
            time_end = float(time.time())               
        long_time = time_end - time_start
        print(long_time,'/n',time_start,'/n',time_end)
        if long_time > 0.005:
            print("dang do lai:")
        else:
            distance = long_time * 17150
            distance = round(distance,2)
            print("distance: ",distance, "cm")
        time.sleep(1)
            
        
except KeyboardInterrupt :
    print("da tat chuong trinh")
    GPIO.cleanup()
        
