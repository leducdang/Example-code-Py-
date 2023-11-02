import time

while int(input("nhan 1 de bat dau:"))== 1:
    time_start= time.time()
    break
    
while int(input("nhan 0 de ket thuc:"))== 0:
    time_end= time.time()
    break

longtime = time_end - time_start
print(longtime)




