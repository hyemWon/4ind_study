import cv2
import numpy as np
import math

circles = np.zeros((4,2), np.int)
counter = 0

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[counter] = x,y
        print(circles)
        counter += 1

        # cv2.circle(img, (x,y), 5, (0,0,255), cv2.FILLED)

if __name__=='__main__':
    img = cv2.imread('./dataset/card1.jpg')

    while True:
        if counter == 4:
            pass
            width, height = 220, 180
            pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])

            width = math.pow(pts1[1][0]-pts1[0][0],2) + math.pow(pts1[1][1]-pts1[0][1],2)
            width = int(math.sqrt(width))
            height = math.pow(pts1[2][0]-pts1[0][0],2) + math.pow(pts1[2][1]-pts1[0][1],2)
            height = int(math.sqrt(height))

            pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

            matrix = cv2.getPerspectiveTransform(pts1,pts2)
            imgOutput = cv2.warpPerspective(img.copy(), matrix, (width, height))

            cv2.imshow("Output Image", imgOutput)
            

        for x in range(4):
            cv2.circle(img, (circles[x][0],circles[x][1]), 3, (0,0,255), cv2.FILLED)

        cv2.imshow('Original Image', img)
        cv2.setMouseCallback("Original Image", mousePoints)
        
        cv2.waitKey(1)
