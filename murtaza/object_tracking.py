#  물체추적

import cv2
import numpy as np

video_path = 'dataset/dance.mp4'
cap = cv2.VideoCapture(video_path)

output_size = (187, 333) # (width, height)

# video writer 초기화
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
print('%s_output.mp4' % (video_path.split('.')[0]))
out = cv2.VideoWriter('%s_output.mp4' % (video_path.split('.')[0]), fourcc, cap.get(cv2.CAP_PROP_FPS), output_size)
# out = cv2.VideoWriter('dataset/dance_output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), output_size)


if not cap.isOpened():
    exit()


# opencv object tracker 
tracker = cv2.TrackerCSRT_create() # 객체 초기화


# 관심영역 설정하기
# 첫번째 프레임 읽기
ret, img = cap.read()

# 윈도우의 이름을 설정한다.
cv2.namedWindow('Select Window')
cv2.imshow('Select Window', img)

# ROI 설정: 드래그해서 스페이스바 누르면 ROI 지정된다. -> 정보가 rect에 저장
# center에서 시작하지 말고, 중심점을 보여라
rect = cv2.selectROI('Select Window', img, fromCenter=False, showCrosshair=True) # (x, y, w, h)
cv2.destroyWindow('Select Window')


# tracker 설정: object tracker가 img와 rect를 따라가게끔 설정
tracker.init(img, rect)


while True:
    ret, frame = cap.read()

    if not ret:
        exit()

    # img에서 rect로 설정한 이미지와 비슷한 물체의 위치를 찾아 반환
    success, box = tracker.update(frame) # 성공여부, left, top, w, h

    left, top, w, h = [int(v) for v in box]

    center_x = left + w/2
    center_y = top + h/2

    result_top = int(center_y - output_size[1] / 2)
    result_bottom = int(center_y + output_size[1] / 2)
    result_left = int(center_x - output_size[0] / 2)
    result_right = int(center_x + output_size[0] / 2)

    result_img = frame[result_top:result_bottom, result_left:result_right].copy()

    out.write(result_img) # 비디오 저장

    cv2.rectangle(frame, pt1=(left, top), pt2=(left + w, top +  h), color=(0,0,0), thickness=3)

    cv2.imshow('result_img', result_img)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break