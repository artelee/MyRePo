import cv2
import numpy as np

# lenna.png 이미지 읽기
image = cv2.imread('lenna.png')

if image is None:
    print("lenna.png 이미지를 찾을 수 없습니다.")
    exit()

# BGR 이미지를 YUV로 변환
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

# YUV 성분 분리
y, u, v = cv2.split(yuv_image)

# 각 성분 출력
print("Y 성분 (Luminance):")
print(y)

print("\nU 성분 (Chrominance, Blue projection):")
print(u)

print("\nV 성분 (Chrominance, Red projection):")
print(v)

# 분리된 성분을 각각 이미지로 표시
cv2.imshow('Y (Luminance)', y)
cv2.imshow('U (Chrominance)', u)
cv2.imshow('V (Chrominance)', v)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()