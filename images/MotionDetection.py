import cv2
import numpy as np
import os
import datetime

cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

alarm_given = 0
alarm_limit = 1

while True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    conturs, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame1, conturs, -1, (0, 255, 0), 1)
    for contour in conturs:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.putText(frame1, "Status: {}".format("Movement!"), (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("Movement Detected! Time: {}".format(datetime.datetime.now()))
        #os.system("Megamind.avi")
        #break


    cv2.imshow("Frame", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    k = cv2.waitKey(10)
    if k == 27 & 0xFF:
        break

cap.release()
cv2.destroyAllWindows()