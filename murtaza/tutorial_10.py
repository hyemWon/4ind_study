# 윤곽선을 찾아 물체의 모양 Detection
# 1) 노이즈 제거 - 가우시안 필터
# 2) 

import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 320,200)
cv2.createTrackbar("Threshold1", "Parameters", 50, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 100, 255, empty)
cv2.createTrackbar("Area", "Parameters", 5000, 50000, empty)


# 하얀색의 객체를 검출 (배경은 검정색, 물체는 흰색)
def getContours(img, imgContour): # (입력이미지, 출력이미지)
    # findContours()를 이용하여 이진화 이미지에서 윤곽선을 검색
    # 윤곽선, 계층 구조 반환
    # contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 관심없는 윤곽선 제외
    for cnt in contours:
        area = cv2.contourArea(cnt) # 폐곡선 형태의 윤곽선으로 둘러싸인 부분의 면적
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMin:
            # 그리기 (이미지, 윤곽선, 윤곽선인덱스, BGR, 두께, 선형타입)
            cv2.drawContours(imgContour, cnt, -1, (255,0,255), 7)
            peri = cv2.arcLength(cnt, True) # 윤곽선 둘레 길이
            # 인자로 주어진 곡선 또는 다각형을 꼭지점 수를 줄여 새로운 곡선이나 다각형 생성
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # 꼭지점 좌표 반환
            # print(len(approx)) # 꼭지점 개수
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0,255,0), 5)

            cv2.putText(imgContour, "Points: " + str(len(approx)), (x+w+20,y+20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x+w+20,y+45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),2)



while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (480, 340), interpolation=cv2.INTER_LINEAR)

    # 가우시안 필터는 에지를 검출하기전에 노이즈를 제거하기 위해 사용
    imgBlur = cv2.GaussianBlur(frame, (7,7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)

    # 캐니 에지 검출
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    # 노이즈 제거 (팽창)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    # 윤곽선(Contour) 검출
    imgContour = frame.copy()
    getContours(imgDil, imgContour)

    imgCanny = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)
    imgDil = cv2.cvtColor(imgDil, cv2.COLOR_GRAY2BGR)
    imgStack1 = np.hstack([frame, imgGray, imgCanny])
    imgStack2 = np.hstack([frame, imgDil, imgContour])


    cv2.imshow("Result1", imgStack1)
    cv2.imshow("Result2", imgStack2)
   

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()