# Week 12 — 최종 정리: AI 기초 과정 통합과 HTML 학습 페이지 운영

## 학습 목표
- 12주 기초 과정을 한 흐름으로 연결한다.
- Markdown 기반 강의자료를 HTML로 배포하는 방법을 이해한다.
- 이후 심화 학습 로드맵을 수립한다.

---

## 1. 우리가 배운 전체 흐름
1. Python 기초 문법과 문제 해결
2. 데이터 전처리와 머신러닝 기초
3. 딥러닝(ANN), CNN, RNN/LSTM
4. Transformer와 LLM(GPT/BERT)
5. ChatGPT 발전 원리(Instruction Tuning + RLHF)
6. RAG 기반 서비스 구현

## 2. Markdown → HTML 연결 방식
- 원본 강의: `curriculum/week01.md` ~ `week12.md`
- 빌드 명령: `python build_curriculum.py`
- 생성 결과: `built/weeks/*.html`, `built/manifest.json`
- `index.html`이 manifest를 읽어 주차별 페이지 로드

## 3. 학습 페이지 운영 팁
- 한 주차 수정 후 즉시 빌드/검수
- 코드 블록, 표, Mermaid 다이어그램 활용
- 주차별 실습 결과를 별도 저장소로 관리

## 4. 다음 단계 로드맵
- 수학 심화: 선형대수/확률/최적화
- 모델 심화: ViT, Diffusion, MoE
- 서비스 심화: 평가 자동화, 모니터링, 비용 최적화

## 최종 미션
1. 자신만의 AI 기초 강의 1주차를 새로 작성.
2. Markdown 수정 후 빌드하여 HTML에서 확인.
3. 배운 모델 중 1개를 선택해 이론/원리 발표 자료 작성.

## 정리
이제 여러분은 AI 학습의 기반 개념과 서비스 구현 흐름을 한 번에 연결할 수 있다.

