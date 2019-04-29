import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (500,300))
    # 파란색과 녹색 부분 제거하기---(*1)
    frame[:, :, 0] = 0 # 파란색을 0으로
    frame[:, :, 1] = 0 # 초록색을 0으로
    cv2.imshow('RED Camera', frame)
    if cv2.waitKey(1) == 13: break

cap.release() # 카메라 해제하기
cv2.destroyAllWindows() # 윈도우 제거하기

