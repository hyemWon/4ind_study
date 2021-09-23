# 다양한 유형의 모양 만들기 & 이미지에 텍스트 만들기

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

print(img)

# img[:] = 255,0,0
# print(img[:])

cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 2)
cv2.rectangle(img, (350,100), (450,200), (0,0,255), cv2.FILLED)
cv2.circle(img, (150,400), 50, (255,0,0), 3)
cv2.putText(img, "Draw Shapes", (75,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 1)

cv2.imshow('image', img)

cv2.waitKey(0)
