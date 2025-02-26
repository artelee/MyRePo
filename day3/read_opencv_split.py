import cv2
import numpy as np

# lenna.png 이미지 읽기
image = cv2.imread('lenna.png')

if image is None:
    print("lenna.png 이미지를 찾을 수 없습니다.")
    exit()

# BGR 채널 분리
blue, green, red = cv2.split(image)

# 각 채널 출력
print("Blue 채널:")
print(blue)

print("\nGreen 채널:")
print(green)

print("\nRed 채널:")
print(red)

# 분리된 채널을 각각 이미지로 표시
cv2.imshow('Blue Channel', blue)
cv2.imshow('Green Channel', green)
cv2.imshow('Red Channel', red)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()