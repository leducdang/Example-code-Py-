import os
from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0)

model = YOLO('yolov5s.pt')  # load a custom model
# model = YOLO('C:/Users/DELL/runs/detect/train7/weights/last.pt')
threshold = 0.1

while True:
    ret, frame = cap.read()
    H, W, _ = frame.shape
    results = model(frame)[0]
    # print (results)
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        print(score)
        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper() +' '+ str("{:.1f}".format(score)) , (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    cv2.imshow("windows", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
