import cv2
import numpy as np

# lenna.png 이미지 읽기
image = cv2.imread('lenna.png')

if image is None:
    print("lenna.png 이미지를 찾을 수 없습니다.")
    exit()

# BGR 이미지를 HSV로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV 성분 분리
hue, saturation, value = cv2.split(hsv_image)

# 각 성분 출력
print("Hue 성분:")
print(hue)

print("\nSaturation 성분:")
print(saturation)

print("\nValue 성분:")
print(value)

# 분리된 성분을 각각 이미지로 표시
cv2.imshow('Hue', hue)
cv2.imshow('Saturation', saturation)
cv2.imshow('Value', value)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()