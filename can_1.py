import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

im = args["image"]
img = cv2.imread(im)
rows, cols, ch = img.shape
dimension = img[1, 1]

if dimension[0] == 184:
    point_one = np.float32([[0, 0], [810, -70], [-670, 533], [800, 803]])
    point_two = np.float32([[0, 0], [650, 0], [0, 533], [650, 537]])
    M = cv2.getPerspectiveTransform(point_one, point_two)
    dst = cv2.warpPerspective(img, M, (800, 533))
    image = dst

if dimension[0] == 150 or dimension[0] == 255:
    image = img.copy()

output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 250, param1=90, param2=80, minRadius=10, maxRadius=100)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

if dimension[0] == 150 or dimension[0] == 255:
    cv2.imshow("Detected Circle", np.hstack([image, output]))
    cv2.waitKey(0)

if dimension[0] == 184:
    new = output
    pts3 = np.float32([[0, 0], [645, 95], [360, 485], [645, 450]])
    pts4 = np.float32([[0, 0], [800, 0], [0, 533], [800, 533]])
    back = cv2.getPerspectiveTransform(pts3, pts4)
    complete = cv2.warpPerspective(new, back, (800, 533))
    og = cv2.warpPerspective(image, back, (800, 533))
    cv2.imshow('Detected Circle', np.hstack([og, complete]))
    cv2.waitKey(0)
