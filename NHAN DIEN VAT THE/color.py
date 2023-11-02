import cv2
import numpy as np
# path = "D:\HocAI\Hoc Python\Resources\lambo.png"
# frame = cv2.imread(path) 
def nothing(x):
    pass

cap = cv2.VideoCapture(0)                                               # tao luong video
# cap.set(3, 500)
# cap.set(4, 400) 
cv2.namedWindow("Trackbars")                                            # tao them 1 khung cua so ten Trackbars

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)               # tạo trackbar de co the dieu chinh gia tri LOW-H
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)             # tạo trackbar de co the dieu chinh gia tri UPER-V

while True:
    _, frame = cap.read()  
    # frame = cv2.imread(path) 
    frame = cv2.GaussianBlur(frame,(5, 5), 0)                                            # Lay hinh anh tu video
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                        # chuyen doi mau hinh anh tu BGR sang HSV

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")                      # lay gia tri vi tri tren cua so Trackbars, tren thanh gia tri L-H gan vao bien l-h
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    
    lower_blue = np.array([l_h,l_s , l_v])                             # tao mang gia tri mau dang HSV muc lower
    upper_blue = np.array([u_h, u_s, u_v])                              # tao mang gia tri mau dang HSV muc upper
    mask = cv2.inRange(hsv, lower_blue, upper_blue)                     #tao anh HSV voi gia trị trong khoang LOWER VA UPPER
    edges = cv2.Canny(mask, 75, 150)
    contours, hierarchy = cv2.findContours(edges,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    cv2.imshow("edges", edges)

    if cv2.waitKey(1) == ord("q"):             # nhan phim "q" de thoat
        break

cap.release()
cv2.destroyAllWindows()