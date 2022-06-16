import cv2 as cv
import os
import numpy as np

img = cv.imread('/Users/yudiz/Desktop/open_cv/a.jpeg')

img = cv.resize(img ,(600, 400))
cv.imshow('lion',img)

cv.waitKey(0)

# -----------------------multiple image slide ------------------------------------
imagespath = os.listdir('images')
path = r"""/Users/yudiz/Desktop/open_cv/images/"""

print(path,"cdcjjjjdnskjfjkshfdjksfhkdjs")

try:
    for i  in imagespath:
        
        if  i == ".DS_Store":
           continue
        else: 
            print(i, "@@@@@@@")
            img_path = path+i
            print(img_path,"££££££££££££££££££££££££££££££££££")
            img  = cv.imread(img_path)
            img = cv.resize(img ,(1200, 900))
            img_2  =  np.hstack((img,img, img))     #  hstack use for one image show multiple time 
        
            img_4 = np.vstack((img_2, img_2))
            cv.imshow('images', img_4)
            
            cv.waitKey(300)    

except Exception as e:
    print(e)


finally:
  print(imagespath)

# ------------------------------one image show multiple time -----------------------------



img = cv.imread('/Users/yudiz/Desktop/open_cv/a.jpeg')

img = cv.resize(img ,(600, 400))

imggray  = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
imgblur = cv.GaussianBlur(imggray, (7,7),0)
imgcanny = cv.Canny(img,100,100)



cv.imshow('lion',imggray)
cv.imshow('s',imgblur)
cv.imshow('liwon',imgcanny)
cv.waitKey(0)


# ------------------------------  crop image   -----------------------------



img = cv.imread('/Users/yudiz/Desktop/open_cv/a.jpeg')

img = cv.resize(img ,(600, 400))

print(img.shape,"nsndsndns")

imgcrop = img[0:100, 200:500]   # crop this image 

cv.imshow('lion',imgcrop)


cv.waitKey(0)