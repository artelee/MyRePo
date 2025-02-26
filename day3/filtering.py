import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('mountain.jpg', cv2.IMREAD_GRAYSCALE)  # Grayscale로 변환하여 읽음

# 1. 평균값 필터 적용
kernel_size = (5, 5)  # 커널 크기
mean_filtered = cv2.blur(image, kernel_size)

# 2. 샤프닝 필터 적용
sharpening_kernel = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, sharpening_kernel)

# 3. 라플라시안 필터 적용
laplacian_filtered = cv2.Laplacian(image, cv2.CV_64F)  # 64F로 사용하는 이유는 더 많은 범위를 표현하기 위해

# 결과 출력
cv2.imshow('Original', image)
cv2.imshow('Mean Filter', mean_filtered)
cv2.imshow('Sharpened', sharpened)
cv2.imshow('Laplacian', cv2.convertScaleAbs(laplacian_filtered))  # 절대값을 정수 이미지로 변환
cv2.waitKey(0)
cv2.destroyAllWindows()