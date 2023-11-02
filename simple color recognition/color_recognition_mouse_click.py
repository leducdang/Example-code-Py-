#https://pysource.com/2021/10/19/simple-color-recognition-with-opencv-and-python/
import cv2          #them thu vien xu ly anh
import numpy as np

#point = np.zeros((4,2),int)
#count = 0
cx, cy = 0, 0


def Event(event, x, y, flag, par):
    global count
    global cx
    global cy
    if event == cv2.EVENT_LBUTTONDOWN:
#        point[count] = x, y
#       count = count + 1
        cx, cy = x, y
    
#    if event == cv2.EVENT_LBUTTONUP:
#        point[count] = x, y
#        count = count + 1
    



cap = cv2.VideoCapture(0)                       #tao luong video
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)         # chinh lai kich thuoc chieu rong khung hinh
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)         # chinh lai kich thuoc chieu cao khung hinh

while True:
    _, frame = cap.read()                                       #lay anh trong luong video de xu ly voi ten khung hinh la "frame"
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)          #chuyen doi anh tu BGR sang HSV
    height, width, _ = frame.shape                              #lay kich thuoc khung hinh
    #print(height,width)                                         # in ra kich thuoc khung hinh
#    cx = int(width / 2)                                         # lay tam vi tri pixel de nhan dien mau
#    cy = int(height / 2)
#    if point[1, 0] != 0:
#        cv2.rectangle(frame, point[0],point[1] , (0, 0, 255), 1)
    cv2.imshow("Frame", frame)
    cv2.setMouseCallback("Frame", Event)
#    print (point)
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]                                 # lay gia tri mau dạng HSVW
    print(hue_value)
                                                                # so danh gia tri lay dươc de xac dinh mau
    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "underfined"

    pixel_center_bgr = frame[cy, cx]
    print(pixel_center_bgr)                                                              #lay gia tri mau tai vi tri lay mau
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])        # xac dinh mau tai BGR tai vi tri lay mau

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)                    # ve khung hien thi mau
    cv2.putText(frame, color, (cx - 200, 100), 0, 1, (b, g, r), 1)                                # viet mau duoc xac dinh
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 2)                                               #tao tam lay mau
    cv2.imshow("Frame", frame)
   
    
    if cv2.waitKey(1)==ord("q"):                                                                  # nhan phim "q" de thoat
        break

cap.release()
cv2.destroyAllWindows()