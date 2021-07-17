import cv2
import numpy as np

cap = cv2.VideoCapture('roll.MOV')
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_number = 0
while frame_number < frames:

    ret1, img1 = cap.read()

    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    detected_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, minDist=20000, param1=200, param2=20, minRadius=70,
                                        maxRadius=140)

    if detected_circles is not None:

        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0]:
            a, b, r = pt[0], pt[1], pt[2]

            cv2.circle(img1, (a, b), r, (118, 5, 255), 9)
            cv2.circle(img1, (a, b), 1, [166, 68, 12], 14)

    cv2.imshow("Rolling Can", img1)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    frame_number += 1

cv2.destroyAllWindows()
cap.release()