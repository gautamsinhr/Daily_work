import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("tracking")

cv2.createTrackbar("lh", "tracking", 0, 255, nothing)
cv2.createTrackbar("ls", "tracking", 0, 255, nothing)
cv2.createTrackbar("lv", "tracking", 0, 255, nothing)
cv2.createTrackbar("uh", "tracking", 255, 255, nothing)
cv2.createTrackbar("us", "tracking", 255, 255, nothing)
cv2.createTrackbar("uv", "tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('b.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #(hue, saturation and value)


    l_h = cv2.getTrackbarPos("lh", "tracking")
    l_s = cv2.getTrackbarPos("ls", "tracking")
    l_v = cv2.getTrackbarPos("lv", "tracking")

    u_h = cv2.getTrackbarPos("uh", "tracking")
    u_s = cv2.getTrackbarPos("us", "tracking")
    u_v = cv2.getTrackbarPos("uv", "tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()