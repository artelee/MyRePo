import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# 1. MNIST 데이터 로드 및 전처리
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 데이터 정규화 (픽셀 값을 0~1 범위로 스케일링)
x_train = x_train / 255.0
x_test = x_test / 255.0

# 레이블을 원-핫 인코딩
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 2. MLP 모델 정의
model = Sequential([
    Flatten(input_shape=(28, 28)),  # 28x28 이미지를 1차원 벡터(784차원)로 변환
    Dense(128, activation='relu'),  # 첫 번째 은닉층 (유닛=128)
    Dense(64, activation='relu'),  # 두 번째 은닉층 (유닛=64)
    Dense(10, activation='softmax')  # 출력층 (클래스=10, softmax)
])

# 3. 모델 컴파일
model.compile(optimizer='adam',  # Adam 옵티마이저
              loss='categorical_crossentropy',  # 다중클래스 분류를 위한 손실 함수
              metrics=['accuracy'])  # 평가 지표로 정확도 사용

# 4. 모델 학습
history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# 5. 테스트 데이터로 모델 평가
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"\n테스트 정확도: {test_acc:.4f}")

# 6. 학습된 모델 저장
model.save('mnist_mlp_model.h5')