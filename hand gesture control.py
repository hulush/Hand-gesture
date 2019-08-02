#Hand gesture recognition
#WeGo Korea
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand.xml')
count = 0
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2,)
    contour = hands
    contour = np.array(contour)
    if count == 0:

        if len(contour) == 2:
            cv2.putText(img=frame, text='Engine started',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(0, 255, 0))

            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            count += 1
    if count > 0:

        if len(contour) >= 2:
            cv2.putText(img=frame, text='Go',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(255, 0, 0))

            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        elif len(contour) == 1:
            cv2.putText(img=frame, text='Go Go',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(0, 255, 0))

            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour) == 0:
            cv2.putText(img=frame, text='STOP',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(0, 0, 255))

        count += 1

    cv2.imshow('Control_frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 30:
        break
