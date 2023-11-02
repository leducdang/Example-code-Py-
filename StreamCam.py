import cv2
cap = cv2.VideoCapture(0)   #chọn luồng camera sử dụng
#cap = cv2.VideoCapture("1.mp4")  nếu ko có camera có thể chọn video bất kì để phát
counter = 10

while True:
    ret, fame = cap.read()
    print(ret)      # tra ve gia tri true neu camera doc duoc anh binh thuong
                    # tra ve false neu khong load dươc camera
    cvfame = cv2.cvtColor(fame,cv2.COLOR_BGR2GRAY)
    width = int (cap.get(3))
    height = int(cap.get(4))       #lay chieu cao
    print(width,height)
    # ve cac hinh len man hinh dang chay
    img = cv2.line(fame,(0,0),(width,height),(255,255,0),3)
    # ve hinh chu nhat
    img = cv2.rectangle(fame,(0,0),(100,100),(123,200,50),-1)   # bỏ -1 thay bằng số nguyên >0 để tạo viền
    # ve hinh tron
    img = cv2.circle(fame,(width//2,height//2),20,(113,90,200),3)
    #ghi chu len khung hinh
    #img = cv2.putText(fame,"test",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(222,222,222),3)
    img = cv2.putText(fame, str(counter), (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (222, 222, 222), 3)

    cv2.imshow("test cam",fame)  #hiển thị hình ảnh đọc được lên khung hình co ten la "test cam"

    if cv2.waitKey(1)==ord("q"):   #thoát chuong trinh khi nhan phim "q"
        break
cap.release()
cv2.destroyAllWindows()