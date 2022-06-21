

import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread('lena.png', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F, ksize=1)
lap = np.uint8(np.absolute(lap))

soblex  = cv.Sobel(img, cv.CV_64F,1,0)
sobley  = cv.Sobel(img, cv.CV_64F,0,1)

soblex = np.uint8(np.absolute(soblex))
sobley = np.uint8(np.absolute(soblex))

soboelcombined = cv.bitwise_or(soblex, sobley) # for combine two image result 

titles = ['image', 'laplacin', 'soblex', 'sobley','soboelcombined']


image  =[img, lap, soblex, sobley,soboelcombined]

for i in range(5):
    plt.subplot(3,2, i+1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()    



