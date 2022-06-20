import cv2 as cv
import numpy as np


img = cv.imread("a.jpg")
img = cv.resize(img,(500,500))

#creat image border 

brdr = cv.copyMakeBorder(img,10,10,5,5,cv.BORDER_CONSTANT,value = [255,0,125])

cv.imshow("res",brdr)
cv.waitKey(0)
cv.destroyAllWindows()