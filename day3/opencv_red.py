import cv2
import numpy as np

# 1. 이미지 읽기
image = cv2.imread("candies.png")

# 2. 이미지를 BGR에서 HSV 색공간으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. 빨간색 HSV 범위 설정
# 빨간색은 Hue 값이 양 끝단(0~10, 160~180)에 걸쳐 있음
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# 4. 빨간색 마스크 생성
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)  # 첫 번째 범위
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)  # 두 번째 범위
red_mask = mask1 | mask2  # 두 마스크를 합침

# 5. 원본 이미지에 마스크 적용하여 빨간색만 추출
red_extracted = cv2.bitwise_and(image, image, mask=red_mask)

# 6. 결과 출력
cv2.imshow("Original Image", image)
cv2.imshow("Red Extracted", red_extracted)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()