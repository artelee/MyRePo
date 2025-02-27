from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

# 1. 웹캠 또는 동영상 파일에서 이미지 캡처
# Open webcam (or replace '0' with the path to a video file)
cap = cv2.VideoCapture(0)

print("웹캠을 열었습니다. ESC를 눌러 종료합니다.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("카메라에서 이미지를 읽어오지 못했습니다. 종료합니다.")
        break

    # 2. 얼굴 감지 및 감정 분석
    try:
        # Processing the frame through DeepFace for emotion analysis
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # 3. 감정 출력 및 화면에 표시
        dominant_emotion = result['dominant_emotion']
        cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    except Exception as e:
        print(f"에러 발생: {str(e)}")

    # Show the frame with the detected emotion
    cv2.imshow("Emotion Detection", frame)

    # Esc 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()