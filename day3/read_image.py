import cv2

# lenna.png 파일 읽기
image = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
# image = cv2.imread('lenna.png', cv2.IMREAD_COLOR)

# 이미지 읽기 확인
if image is None:
    print("이미지를 읽는 데 실패했습니다. 파일 이름이나 경로를 확인하세요.")
else:
    # 창에 이미지 출력
    cv2.imshow('Lenna', image)

    # 키 입력 대기 (0은 무한정 대기)
    cv2.waitKey(0)

    # 모든 창 닫기
    cv2.destroyAllWindows()