# Week 01 — AI 시대를 위한 컴퓨터와 Python 입문

## 학습 목표
- 컴퓨터의 입력·처리·저장·출력 흐름을 설명한다.
- Python 실행 구조와 개발 환경(Colab, IDE, VS Code)을 이해한다.
- 변수, 자료형, 조건문, 반복문으로 기초 코드를 작성한다.

---

## 1. 왜 Python으로 AI를 시작할까?
- 문법이 단순해 초급자가 배우기 쉽다.
- 데이터 분석(NumPy, pandas), 시각화(matplotlib), AI(PyTorch, TensorFlow) 생태계가 크다.
- 실무와 교육 자료가 풍부해 학습 속도가 빠르다.

## 2. 컴퓨터의 기본 동작
| 단계 | 설명 | Python 예시 |
|---|---|---|
| 입력(Input) | 키보드/파일/API로 데이터 받기 | `input()`, `open()` |
| 처리(Processing) | 계산/조건 판단/모델 연산 | `if`, `for`, 함수 |
| 저장(Storage) | 메모리/파일/DB에 보관 | 변수, `.txt`, SQL |
| 출력(Output) | 화면/파일/웹으로 결과 전달 | `print()`, HTML |

## 3. Python 학습 환경 안내
### 3.1 Google Colab (처음 시작 추천)
- 설치 없이 브라우저에서 바로 Python 실행 가능
- 실습 공유가 쉽고, GPU 환경도 간단히 사용 가능
- 초급자는 Colab으로 문법 감을 먼저 익히기 좋다

### 3.2 IDE(통합개발환경)란?
- 코드를 작성·실행·디버깅·확장 기능 관리까지 한 번에 지원하는 개발 도구
- Python 학습이 깊어지면 IDE 사용이 생산성을 크게 높여준다

### 3.3 기본 권장 IDE: VS Code
- 가볍고 확장성이 좋아 Python + 웹 + AI 학습에 적합
- Python 확장, Jupyter 확장, Git 연동이 편리
- 본 과정에서는 기본적으로 VS Code 사용을 권장한다

## 4. Python 기초 문법
### 4.1 변수와 자료형
```python
name = "AI Learner"
age = 20
score = 91.5
is_ready = True
```

### 4.2 조건문
```python
if score >= 90:
    level = "Excellent"
else:
    level = "Keep Going"
print(level)
```

### 4.3 반복문
```python
for n in range(1, 6):
    print("step", n)
```

## 5. 실습 미션
1. 이름, 나이, 관심 분야를 입력받아 자기소개를 출력한다.
2. 점수를 입력받아 A/B/C 등급을 계산한다.
3. 1부터 10까지 합계를 반복문으로 구한다.
4. Colab에서 작성한 코드를 VS Code에서도 실행해본다.

## 정리
이번 주차는 AI 학습의 출발점으로, 컴퓨터의 동작 원리와 Python 기본 문법, 그리고 Colab/IDE/VS Code 개발 환경의 차이를 익혔다.
