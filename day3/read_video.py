import cv2

# 입력 비디오 이름
input_file = "test_video.mp4"

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(input_file)

# 비디오 출력 설정
output_file = "output_video.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정 (XVID)
fps = int(cap.get(cv2.CAP_PROP_FPS))  # 원본 영상 FPS 가져오기
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 프레임 너비
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 프레임 높이

out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# 비디오 파일 열리지 않을 경우 예외 처리
if not cap.isOpened():
    print("비디오 파일을 열 수 없습니다. 파일 이름을 확인하세요.")
    exit()

print("비디오 처리를 시작합니다...")

# 프레임 읽기 및 처리
while True:
    ret, frame = cap.read()
    if not ret:
        print("비디오를 모두 처리했습니다.")
        break

    # 영상을 흑백으로 변환하는 로직(선택 사항: 주석 제거 시 활성화)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 결과를 출력 파일에 작성
    out.write(frame)

    # 현재 프레임을 화면에 표시
    cv2.imshow("Video Frame", frame)

    # ESC 키로 중지 (27은 ESC 키의 ASCII 코드)
    if cv2.waitKey(1) & 0xFF == 27:
        print("처리가 사용자에 의해 중단되었습니다.")
        break

# 모든 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"비디오 처리가 완료되었습니다. 저장된 파일: {output_file}")