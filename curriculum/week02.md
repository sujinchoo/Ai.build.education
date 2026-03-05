# Week 02 — Python 핵심 문법 심화와 문제 해결

## 학습 목표
- 함수, 리스트, 딕셔너리, 예외 처리의 의미를 이해한다.
- 작은 문제를 절차적으로 분해해 코드로 구현한다.
- AI 전처리에 필요한 문자열/리스트 처리를 연습한다.

---

## 1. 함수(Function): 재사용 가능한 블록
```python
def normalize_score(score, max_score=100):
    return round(score / max_score, 3)

print(normalize_score(87))
```

## 2. 컬렉션 자료구조
- 리스트(list): 순서가 있는 데이터 묶음
- 튜플(tuple): 수정이 어려운 고정 데이터
- 딕셔너리(dict): key-value 기반 데이터

```python
student = {"name": "Jin", "python": 85, "math": 90}
avg = (student["python"] + student["math"]) / 2
print(avg)
```

## 3. 예외 처리
```python
try:
    x = int(input("숫자 입력: "))
    print(100 / x)
except ValueError:
    print("정수를 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
```

## 4. 알고리즘 사고 연습
- 문제 정의 → 입력/출력 설계 → 예외 케이스 확인 → 구현 → 테스트

## 실습 미션
1. 학생 점수 리스트의 평균/최대/최소를 함수로 작성.
2. 문장 빈도수 카운터(딕셔너리) 작성.
3. 잘못된 입력을 처리하는 계산기 작성.

## 정리
AI 모델 이전에, 데이터 처리와 안정적 코드를 위한 Python 기본기를 단단히 만든다.

