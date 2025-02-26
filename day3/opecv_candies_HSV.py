import cv2
import numpy as np

# 이미지를 읽어옵니다.
image = cv2.imread("candies.png")

# 이미지를 HSV 색상 공간으로 변환합니다.
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 빨간색의 HSV 범위를 설정합니다.
# 빨간색은 HSV 색상 공간에서 두 범위로 나누어 처리해야 합니다.
# lower_red1 = np.array([0, 120, 70])  # 첫 번째 빨간색 범위 (Hue가 낮은 값)
# upper_red1 = np.array([10, 255, 255])
# lower_red2 = np.array([170, 120, 70])  # 두 번째 빨간색 범위 (Hue가 높은 값)
# upper_red2 = np.array([180, 255, 255])
#
# # 두 범위 모두에 대해 마스크를 생성합니다.
# mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)  # 범위 1에 해당하는 마스크
# mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)  # 범위 2에 해당하는 마스크
#
# # 두 마스크를 합칩니다.
# red_mask = cv2.bitwise_or(mask1, mask2)
#
# # 원본 이미지에서 빨간색 부분만 추출합니다.
# result = cv2.bitwise_and(image, image, mask=red_mask)
#
# # 결과를 화면에 띄웁니다.
# cv2.imshow("Original Image", image)
# cv2.imshow("Red Mask", red_mask)
# cv2.imshow("Extracted Red Color", result)
#
# # 키 입력을 기다린 다음 창을 닫습니다.
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 파란색의 HSV 범위를 설정합니다.
# Hue 값은 대략 100 ~ 140으로 설정합니다.
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

# 파란색 범위에 해당하는 마스크를 생성합니다.
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# 원본 이미지에서 파란색 부분만 추출합니다.
result = cv2.bitwise_and(image, image, mask=blue_mask)

# 결과를 화면에 띄웁니다.
cv2.imshow("Original Image", image)
cv2.imshow("Blue Mask", blue_mask)
cv2.imshow("Extracted Blue Color", result)

# 키 입력을 기다린 다음 창을 닫습니다.
cv2.waitKey(0)
cv2.destroyAllWindows()
