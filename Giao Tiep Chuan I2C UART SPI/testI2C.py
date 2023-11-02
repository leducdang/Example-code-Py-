import smbus
from time import sleep
 
bus = smbus.SMBus(1)
 
addr = 0x08
val = 2
 
while True:    
    bus.write_byte(addr, val)
    sleep(1)
    data = bus.read_byte(addr)
    print(data)
    sleep(1)