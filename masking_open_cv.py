import cv2 as cv 
import numpy as np


low_green  = np.array([24 ,24, 123])
high_green = np.array([102,255,255])

# low_orange = np.array([5, 50, 50])
# high_orange = np.array([15, 255, 255])

cap  = cv.VideoCapture(0)

while True:
    ret , frame  =  cap.read()
    cv.imshow('orignal frame', frame)
    
    hsv  =cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    mask = cv.inRange(hsv, low_green ,high_green)
    cv.imshow('masked frame ', mask)
    
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()



