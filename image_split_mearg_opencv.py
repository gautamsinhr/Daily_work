import numpy as np 
import cv2 as cv 

# img = cv.imread('images.jpg')
img = cv.imread('a.jpg')

print(img.shape,'....return in tuple  rows colums and channe')   # return in tuple  rows colums and channels
print(img.size,'.....return total number of pixels is acces')   # return total number of pixels is accessed
print(img.dtype,'......return image datatypes is obtained')  # return image datatypes is obtained

b,g,r = cv.split(img)
img = cv.merge((b,g,r))


img = cv.resize(img , (1000,1000))
# img2 = cv.resize(img2 , (512,512))

# dst = cv.addWeighted(img , .4, img2, .5,0)

# ball = img[154:147, 178:143]
# img[33:143, 59:141] = ball

# 132 176

# 301:85 465:261

# roi = img[389:521, 549:725]
roi = img[85:261, 301:465]

img[85:261, 500:664] = roi

# img[389:521, 730:906]  = roi
# img[389:521, 202:378]  = roi

cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()



# //////////////////////////////////

