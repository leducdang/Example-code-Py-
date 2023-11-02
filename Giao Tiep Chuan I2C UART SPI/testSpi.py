import spidev
import time

spi= spidev.SpiDev()    #tao doi tuong spi
spi.open(0,0)     #mo port0, device 0
spi.max_speed_hz = 500000

try:
    while True:
 #       print("abc")
        resp = spi.xfer2([0x60,0x00,0x00,0x00,0x00])
        c = spi.readbytes(5)
        for x in c:
            print ("nhan:",chr(x))
        time.sleep(1)
except KeyboardInterrupt:
    print("hoan thanh chuong trinh")
    spi.close()