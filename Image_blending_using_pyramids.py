import cv2 as cv 

import numpy as np

apple = cv.imread('lol.jpeg')
orange  = cv.imread('lol2.jpeg')


apple = cv.resize(apple, (500,500))
orange  = cv.resize(orange, (500,500))
print(apple.shape)
print(orange.shape)

apple_orange_half = np.hstack((apple[:,:250], orange[:,250:]))


# #  genrate gaussian pyramid for apple 
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)


# # generate Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)


# # generate Laplacian Pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)


# # generate Laplacian Pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

# # Now add left and right halves of images in each level

apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
    
# # now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)

a = cv.imshow('apples',apple)
b = cv.imshow("orange",orange)
c =cv.imshow('combine',apple_orange_half)






cv.imshow("apple", apple)
cv.imshow("orange", orange)
cv.imshow("apple_orange", apple_orange_half)
# cv.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
cv.waitKey(0)

