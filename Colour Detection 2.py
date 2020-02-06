import cv2
import numpy as np

a = np.zeros([480, 640, 3], np.uint8)

img = cv2.imread('B&W.jpg', 1)
b = cv2.rectangle(a, (200, 0), (450, 200), (255, 255, 255), -1)
bit = cv2.bitwise_and(a, img)
bit1 = cv2.bitwise_or(a, img)
bit2 = cv2.bitwise_not(a, img)
bit3 = cv2.bitwise_xor(a, img)

cv2.imshow("IMAGE", img)
cv2.imshow("BLACK", a)
cv2.imshow("Error", bit2)
cv2.waitKey(0)

cv2.destroyAllWindows()
