import ADS1115
import time

ads = ADS1115.ADS1115()
try:
    while True:
        volt = ads.readADCSingleEnded()
        
        print("{:.0f} mV mesuré sur AN0".format(volt))
        
        temp = volt/10
        print("{:.1f}*c".format(temp))
        
        time.sleep(0.1)
    
except KeyboardInterrupt as e:
    print("chuong trinh da hoan thanh")