import cv2
import numpy as np


def donothing(x):
    pass


cv2.namedWindow('Tracker')

cv2.createTrackbar('LH', 'Tracker', 0, 255, donothing)
cv2.createTrackbar('LS', 'Tracker', 0, 255, donothing)
cv2.createTrackbar('LV', 'Tracker', 0, 255, donothing)

cv2.createTrackbar('UH', 'Tracker', 255, 255, donothing)
cv2.createTrackbar('US', 'Tracker', 255, 255, donothing)
cv2.createTrackbar('UV', 'Tracker', 255, 255, donothing)

while True:
    original_img = cv2.imread('Color.jpg', 1)
    cv2.imshow('Original Image', original_img)

    hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
    # cv2.imshow('HSV Image', hsv_img)

    lhv = cv2.getTrackbarPos('LH', 'Tracker')
    lsv = cv2.getTrackbarPos('LS', 'Tracker')
    lvv = cv2.getTrackbarPos('LV', 'Tracker')
    uhv = cv2.getTrackbarPos('UH', 'Tracker')
    usv = cv2.getTrackbarPos('US', 'Tracker')
    uvv = cv2.getTrackbarPos('UV', 'Tracker')

    lower_bound = np.array([lhv, lsv, lvv])
    upper_bound = np.array([uhv, usv, uvv])

    mask = cv2.inRange(hsv_img, lower_bound, upper_bound)
    cv2.imshow('Mask Image', mask)

    if cv2.waitKey(1) & 0XFF == 27:
        break
cv2.destroyAllWindows()