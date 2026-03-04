# Week 07 — Transformer 기초 확장

## 학습 목표
- Self-Attention의 Q/K/V 개념을 설명할 수 있다.
- Multi-Head Attention의 필요성을 설명할 수 있다.
- Transformer가 RNN 대비 갖는 장점을 설명할 수 있다.

---

## 1. Transformer가 바꾼 것

Transformer는 순차 처리 중심의 RNN과 달리, 문장 전체를 한 번에 보며 병렬 계산이 가능합니다.
이 덕분에 학습 속도와 성능이 크게 향상되었습니다.

---

## 2. Self-Attention 이해

각 단어가 문장 안의 다른 단어들과 얼마나 관련 있는지 계산합니다.

- Query: 지금 내가 찾고 싶은 정보
- Key: 내가 가진 정보의 특징
- Value: 실제 전달할 정보

관련도 점수를 기반으로 단어 표현을 갱신합니다.

---

## 3. Multi-Head Attention

한 번의 Attention만 쓰면 문맥을 단일 관점으로만 봅니다.
여러 Head를 사용하면 문법, 의미, 거리 등 다양한 관점을 동시에 학습할 수 있습니다.

---

## 4. Positional Encoding

Transformer는 순서를 직접 처리하지 않기 때문에, 위치 정보를 숫자로 추가해야 합니다.
이것이 Positional Encoding입니다.

---

## 5. 실습 아이디어

짧은 문장에서 Attention 가중치를 시각화해 어떤 단어가 중요한지 확인합니다.

---

## 정리
- Transformer의 핵심은 Self-Attention이다.
- Multi-Head는 표현력을 높이는 장치다.
- 병렬 처리 덕분에 대규모 학습에 유리하다.
