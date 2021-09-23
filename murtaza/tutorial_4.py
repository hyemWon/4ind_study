# Multiple Imag es to Display
# 넘파이의 스태킹 기능

import cv2
import numpy as np

img1 = cv2.imread('/home/fourind/dataset/img/soccer.jpg',0)
img2 = cv2.imread('/home/fourind/dataset/img/ball.jpg')
print(img1.shape)
print(img2.shape)

# dsize가 (0,0)이면 fx, fy 을 이용하여 결정 (스케일 비율)
img1 = cv2.resize(img1, (0,0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0,0), None, 0.5, 0.5)

img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

hor = np.hstack((img1, img2))
ver = np.vstack((img1, img2))

cv2.imshow('Vertical', ver)
cv2.imshow('Horizontal', hor)


cv2.waitKey(0)

