import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lenna 이미지를 읽어옵니다.
image = cv2.imread("lenna.png")

# 이미지를 제대로 확인하기 위해 BGR -> RGB로 변환(Matplotlib는 RGB를 사용)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 히스토그램 계산 - B, G, R 채널 각각
colors = ('b', 'g', 'r')  # OpenCV에서 기본 채널 순서: Blue, Green, Red
for i, color in enumerate(colors):
    # 각 채널에 해당하는 히스토그램 계산 (채널 인덱스, 범위: [0, 256])
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    # 히스토그램 플롯
    plt.plot(hist, color=color, label=f'{color.upper()} Channel')

# 그래프 속성 설정
plt.title("BGR Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend(loc='upper right')

# 그래프 시각화
plt.show()