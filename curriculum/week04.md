# Week 04 — Machine Learning 기초 확장

## 학습 목표
- 머신러닝과 규칙 기반 프로그래밍의 차이를 설명할 수 있다.
- 분류와 회귀 문제를 구분할 수 있다.
- scikit-learn으로 학습-예측-평가 흐름을 실습할 수 있다.

---

## 1. 머신러닝의 핵심 아이디어

기존 규칙 기반은 사람이 규칙을 직접 작성합니다.
머신러닝은 데이터에서 패턴을 학습해 규칙을 스스로 만듭니다.

---

## 2. 분류와 회귀

- 분류(Classification): 범주 예측 (예: 합격/불합격)
- 회귀(Regression): 연속값 예측 (예: 집값)

문제 유형을 먼저 정하는 것이 모델 선택의 출발점입니다.

---

## 3. 기본 학습 절차

1) 데이터 수집  
2) 전처리  
3) 학습/검증 데이터 분할  
4) 모델 학습  
5) 예측 및 평가

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
```

---

## 4. 평가 지표 이해

- 정확도(Accuracy)
- 정밀도(Precision)
- 재현율(Recall)
- F1-score

정확도만 보면 데이터 불균형 문제를 놓칠 수 있으므로 함께 해석해야 합니다.

---

## 5. 실습 아이디어

학생 성적 데이터로 합격 여부를 분류하고, 어떤 특성이 결과에 영향을 주는지 해석해봅니다.

---

## 정리
- 머신러닝은 데이터 기반 예측 시스템이다.
- 문제 유형(분류/회귀) 구분이 중요하다.
- 성능 평가는 지표를 함께 봐야 신뢰할 수 있다.
