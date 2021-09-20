# 특정 색상 영역 추출
import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

# 트랙바 이벤트 함수
# BGR -> HSV
# Hue(색상): 0~179, Saturation(채도): 0~255, Value(명도): 0~255

def empty():
    pass

cv2.namedWindow('HSV')
cv2.resizeWindow('HSV', 640, 240)
cv2.createTrackbar('HUE Min', 'HSV', 0, 179, empty)
cv2.createTrackbar('HUE Max', 'HSV', 179, 179, empty)
cv2.createTrackbar('SAT Min', 'HSV', 0, 255, empty)
cv2.createTrackbar('SAT Max', 'HSV', 255, 255, empty)
cv2.createTrackbar('VALUE Min', 'HSV', 0, 255, empty)
cv2.createTrackbar('VALUE Max', 'HSV', 255, 255, empty)

while True:
    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos('HUE Min', 'HSV')
    h_max = cv2.getTrackbarPos('HUE Max', 'HSV')
    s_min = cv2.getTrackbarPos('SAT Min', 'HSV')
    s_max = cv2.getTrackbarPos('SAT Max', 'HSV')
    v_min = cv2.getTrackbarPos('VALUE Min', 'HSV')
    v_max = cv2.getTrackbarPos('VALUE Max', 'HSV')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img,img,mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, result])
    # cv2.imshow('Original', img)
    # cv2.imshow('Hsv', imgHsv)
    # cv2.imshow('mask', mask)
    # cv2.imshow('result', result)
    cv2.imshow('Horizontal Image', hstack)
    

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()