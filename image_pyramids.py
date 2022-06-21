# two types of image pyramid 

# 1 . Gaussian pyramid
# 2 . Laplacian pyramid


# 
# 1 . Gaussian pyramid
import cv2 as cv
from cv2 import imshow 

img = cv.imread('op.jpeg')

# lr1 = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr1)
# # lr3 = cv.pyrDown(lr2)
# hr2 = cv.pyrUp(lr2)

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i), layer)

layer  = gp[5]

cv.imshow("upper level gaussian pytamid", layer)
lp = [layer]
for i in range(5 ,0, -1):
    gaussian_ext = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_ext)
    cv.imshow(str(i), laplacian)





cv.imshow("original image", img)
# cv.imshow("pyrdown 1 image", lr1)
# cv.imshow("pyrdown 2 image", lr2)
# cv.imshow("pyrdown 11 image", hr2)
cv.waitKey(0)
cv.destroyAllWindows()






