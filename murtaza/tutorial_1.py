# 이미지 블러링
# 이미지에 커널(마스크)를 컨볼루션하여 블러링, 샤프닝 등의 처리를 할 수 있다.
# 커널을 직접 만드는 번거로움을 줄이기 위해 OpenCV는 블러링 함수를 제공
# Canny 에지 검출 알고리즘 5단계
# 1) 가우시안 필터로 이미지 노이즈 제거
# 2) Sobel 필터로 Gradient의 크기 구하기
# 3) Non-maximum suppression을 적용하여 에지 검출기에서 거짓 제거
# 4) 에지로 가능성 있는 픽셀을 골라내기 위해 double threshold 방식 적용
# 5) double threshold 방식에서 maxVal을 넘은 부분을 strong edge, minVal와 maxVal 사이의 부분을 weak edge로 설정하여
#    strong edge와 연결되어 있는 weak edge를 edge로 판단하고 그렇지 않는 부분은 제거

import cv2
import numpy as np

URL = 'rtsp://admin:4ind331%23@192.168.0.242/profile2/media.smp'
PATH = '/home/fourind/dataset/'

kernel = np.ones((5,5), np.uint8)
print(kernel)

if __name__ == '__main__':
    # cap = cv2.VideoCapture(PATH)
    #
    # print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    # print(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    #
    # while True:
    #     ret, frame = cap.read()
    #     frame = cv2.resize(frame, (640, 360))
    #     cv2.imshow('frame', frame)
    #
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

    img = cv2.imread(PATH + 'img/soccer.jpg', 0) # 흑백이미지로 읽음
    img = cv2.imread(PATH + 'img/soccer.jpg')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 평균 블러링: nxn 범위 내 이웃 픽셀의 평균을 결과 이미지의 픽셀값으로한다.
    imgBlur1 = cv2.blur(img, (5,5))
    # 가우시안 블러링: 모든 픽셀에 똑같은 가중치를 부여했던 평균 블러링과 달리 가우시안 블러링은 중심에 있는 픽셀에 높은 가중치를 부여
    # 평균 블러링은 에지 포함해서 전체적으로 블러링되는 반면 가우시안 블러링은 에지가 남아있는 상태에서 블러링이 이루어짐
    # 보통 Canny(캐니)로 에지를 검출하기전에 노이즈를 제거하기 위해 사용된다.
    imgBlur2 = cv2.GaussianBlur(img, (7,7), 0)

    # 에지 검출
    # 노이즈 제거한 이미지, threshold1, threshold2
    # 일반적으로 threshold1를 threshold2 보다 작게 지정한다.
    # threshold1과 threshold2 중에서 큰 값은 strong edge를 구하기 위한 임계값, 작은 값은 weak edge를 구하기 위한 임계
    imgCanny = cv2.Canny(imgBlur2, 100, 100)

    # 침식, 팽창 연산
    # 침식: 객체 외각을 깍아내는 연산. 객체 크기는 감소하고 배경은 확대 -> 작은크기의 객체(노이즈) 제거 효과 & 겹쳐 있는 물체를 떼어내는 데도 효과적
    # 팽창: 객체 외각을 확대시키는 연산. -> 객체 안쪽의 노이즈 제거 효과
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=1)


    # cv2.imshow('blur_Mean', imgBlur1)
    # cv2.imshow('blur_Gaussian', imgBlur2)
    cv2.imshow('Edge', imgCanny)
    cv2.imshow('Dilation', imgDilation)
    cv2.imshow('Erode', imgEroded)
    cv2.imshow('Image', img)
    # cv2.imshow('gray', imgGray)

    cv2.waitKey(0)

