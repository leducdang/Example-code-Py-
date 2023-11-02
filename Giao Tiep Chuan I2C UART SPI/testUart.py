import serial
import time

ser = serial.Serial(
    port= '/dev/ttyAMA0',
    baudrate= 9600,
    parity= serial.PARITY_NONE,
    stopbits= serial.STOPBITS_ONE,
    bytesize= serial.EIGHTBITS,
    timeout= 1,
    )

print("Raspberry Pi sending:")

try:
    while True:      
        string = input()
        value = bytes(string,'utf-8')
        print(value)
        ser.write(value)
        ser.flush()
        s=ser.readline()
        data=s.decode()      
        print(data)
        time.sleep(1)
except KeyboardInterrupt:
    print("chuong trinh da hoan thanh")
    ser.close()

