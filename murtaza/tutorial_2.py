# Crop & Resize
import cv2

path = '/home/fourind/dataset/img/soccer.jpg'

img = cv2.imread(path)
print(img.shape)

# Resize
width, height = 400, 400
imgResize = cv2.resize(img, (width, height))
print(imgResize.shape)

# Crop
imgCropped = img[150:480, 250:]
imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))


cv2.imshow('Soccer', img)
cv2.imshow('Resize', imgResize)
cv2.imshow('Crop', imgCropped)
cv2.imshow('Crop & Resize', imgCropResize)

cv2.waitKey(0)