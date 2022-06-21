#  flter of diffrent difrent 
# homogeneous filter , gaussian filter  ,median filter , bilateral filter 
# open cv  read  bgr and matplot lib  read rgb image

#  low pass filter removing noises bluring the image 
#  high pass filter finding edges in the images 
#  gaussian filter is different weight kernel in both x , y direction  

# median  filter is that replace each pixels value with the median 
# of its neighborign pixels . this method is great when dealing with 'salt and pepper noise'

import cv2 as cv

import numpy as np
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# img = cv.imread('op.jpeg')
img = cv.imread('lena.png')
img = cv.cvtColor(img , cv.COLOR_BGR2RGB)
print('yoyo')
kernel  =np.ones((5,5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img,(5,5))
gblur  = cv.GaussianBlur(img, (5,5), 0)
median = cv.medianBlur(img,5)
bilateralfilter = cv.bilateralFilter(img ,1, 75, 75)


titles  = ['image', '2d convolution', 'blur', 'GaussianBlur','median',"bilateralfilter"]
images = [img , dst, blur, gblur, median, bilateralfilter]


for i in  range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()







