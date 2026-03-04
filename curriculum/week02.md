# Week 02 — Python 프로그래밍 기초 확장

## 학습 목표
- 변수와 자료형을 실제 문제에 맞게 선택하여 사용할 수 있다.
- 리스트와 반복문으로 여러 데이터를 효율적으로 처리할 수 있다.
- 조건문과 함수로 읽기 쉽고 재사용 가능한 코드를 작성할 수 있다.

---

## 1. Python 문법을 왜 먼저 배우는가?

Python은 문법이 간결하고 가독성이 높아, 프로그래밍의 핵심 사고를 익히기에 좋습니다.
이번 주는 "작동하는 코드"를 넘어서 "설명 가능한 코드"를 목표로 합니다.

---

## 2. 변수와 자료형

### 2.1 변수
변수는 데이터를 저장하는 이름표입니다.

```python
name = "Jisoo"
age = 17
```

### 2.2 자료형
- `str`: 문자열
- `int`: 정수
- `float`: 실수
- `bool`: 참/거짓
- `list`: 여러 값을 순서대로 저장

```python
print(type(name))
print(type(age))
```

---

## 3. 리스트와 반복문

리스트는 여러 개의 값을 한 번에 다룰 때 가장 기본이 되는 자료구조입니다.

```python
scores = [88, 72, 95, 61]
for score in scores:
    print(score)
```

### 핵심 포인트
- 인덱스는 `0`부터 시작
- `for`문은 반복 작업 자동화에 필수

---

## 4. 조건문으로 의사결정하기

```python
score = 72

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C 이하")
```

조건문은 프로그램이 상황에 따라 다른 행동을 하도록 만듭니다.

---

## 5. 함수로 코드 구조화하기

함수는 반복되는 로직을 묶는 도구입니다.

```python
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"
```

```python
for s in [95, 81, 67]:
    print(s, grade(s))
```

---

## 6. 통합 예제: 학생 성적 리포트

```python
students = [
    {"name": "민수", "score": 92},
    {"name": "지연", "score": 78},
    {"name": "하늘", "score": 85},
]

def pass_or_fail(score):
    return "합격" if score >= 80 else "보완 필요"

for st in students:
    print(f"{st['name']} - {st['score']}점 - {pass_or_fail(st['score'])}")
```

이 예제는 변수, 자료형, 리스트, 조건문, 함수를 모두 연결합니다.

---

## 정리
- 변수와 자료형은 프로그램의 데이터 모델을 만든다.
- 리스트와 반복문은 대량 데이터를 처리하게 해준다.
- 조건문과 함수는 코드의 논리성과 재사용성을 높여준다.
