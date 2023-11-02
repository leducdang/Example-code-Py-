import smbus
from time import sleep
 
bus = smbus.SMBus(1)
 
addr = 0x70
val = 0x51
while True:
    bus.write_byte(addr, val)
    sleep(0.1)
    data_gyus = bus.read_i2c_block_data(addr, 0,2)
    distance = (data_gyus[0]<<8) +data_gyus[1]
    print(data_gyus, distance)
    sleep(1)