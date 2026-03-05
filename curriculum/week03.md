# Week 03 — 데이터 다루기: NumPy와 pandas 기초

## 학습 목표
- 배열/테이블 데이터를 다루는 이유를 이해한다.
- NumPy로 수치 연산을 수행한다.
- pandas로 CSV를 읽고 기초 전처리를 수행한다.

---

## 1. 데이터 과학 워크플로우
수집 → 정제 → 탐색 → 모델 학습 → 평가 → 배포

## 2. NumPy 핵심
```python
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.mean(), arr.std())
```

- 벡터화 연산으로 속도 향상
- 행렬 계산은 딥러닝의 기반

## 3. pandas 핵심
```python
import pandas as pd

df = pd.DataFrame({
    "hours": [1, 2, 3, 4],
    "score": [55, 65, 78, 90]
})
print(df.describe())
```

## 4. 전처리 기본
- 결측치 처리: `dropna()`, `fillna()`
- 범주형 인코딩: one-hot
- 스케일링: 표준화(z-score), 정규화(min-max)

## 실습 미션
1. CSV를 읽고 결측치를 평균으로 대체.
2. 상관관계를 계산하고 학습에 쓸 컬럼 선택.
3. 학습/검증 데이터 분리(train/test split).

## 정리
좋은 모델은 좋은 데이터에서 시작한다. 오늘은 ML 이전 단계인 데이터 준비 역량을 강화했다.

