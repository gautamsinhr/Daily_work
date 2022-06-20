import cv2 as cv
import numpy as np

img = cv.imread('a.jpg', 0)

img = cv.resize(img , (500,500))

th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

th3 = cv.threshold(img, 200, 255, cv.THRESH_TRUNC)
th4 = cv.threshold(img, 127, 200, cv.THRESH_TOZERO)
th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow("image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()