# Week 12 — HTML/CSS/JavaScript 핵심 이론과 필수 코드

## 학습 목표
- HTML 문서 구조와 주요 태그의 역할을 설명한다.
- CSS로 레이아웃과 시각 스타일을 적용하는 원리를 이해한다.
- JavaScript의 동작 방식과 브라우저 실행 원리를 기초 수준에서 설명한다.

---

## 1. HTML 이론: 웹페이지의 뼈대
HTML(HyperText Markup Language)은 웹페이지의 구조를 정의하는 마크업 언어다.

### 1.1 HTML 문서의 기본 구조
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>문서 제목</title>
</head>
<body>
  <h1>안녕하세요</h1>
  <p>첫 웹페이지입니다.</p>
</body>
</html>
```

### 1.2 자주 사용하는 필수 태그
- 제목: `<h1>` ~ `<h6>`
- 본문 텍스트: `<p>`, `<span>`, `<strong>`
- 링크/이미지: `<a>`, `<img>`
- 목록: `<ul>`, `<ol>`, `<li>`
- 구역 나누기: `<div>`, `<section>`, `<header>`, `<footer>`, `<main>`
- 입력 폼: `<form>`, `<input>`, `<button>`, `<label>`

## 2. HTML 기초 실습 코드
```html
<body>
  <header>
    <h1>AI 학습 노트</h1>
  </header>

  <main>
    <section>
      <h2>오늘의 목표</h2>
      <ul>
        <li>HTML 구조 이해</li>
        <li>CSS로 스타일 적용</li>
        <li>JS로 상호작용 만들기</li>
      </ul>
    </section>

    <section>
      <h2>문의</h2>
      <form>
        <label for="email">이메일</label>
        <input id="email" type="email" placeholder="you@example.com" />
        <button type="submit">제출</button>
      </form>
    </section>
  </main>
</body>
```

## 3. CSS 설명: 스타일을 입히는 원리
CSS(Cascading Style Sheets)는 HTML 요소에 색상, 크기, 배치, 반응형 동작을 적용한다.

### 3.1 CSS 기본 문법
```css
selector {
  property: value;
}
```

### 3.2 필수 CSS 코드 예시
```css
body {
  font-family: "Noto Sans KR", sans-serif;
  margin: 0;
  padding: 24px;
  background: #f8fafc;
}

h1 {
  color: #1d4ed8;
}

.card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 16px;
}

button {
  background: #2563eb;
  color: white;
  border: none;
  padding: 10px 14px;
  border-radius: 8px;
}
```

### 3.3 CSS 핵심 개념
- 선택자(Selector): 어떤 HTML 요소에 스타일을 적용할지 지정
- 박스 모델(Box Model): content + padding + border + margin
- 캐스케이딩(Cascade): 우선순위 규칙으로 최종 스타일 결정
- 레이아웃: `display`, `position`, `flex`, `grid`로 화면 배치

## 4. JavaScript 설명 및 동작 원리
JavaScript는 웹페이지를 동적으로 바꾸고 사용자와 상호작용하게 만드는 프로그래밍 언어다.

### 4.1 JavaScript가 하는 일
- 버튼 클릭, 입력값 검증, 모달 열기/닫기
- API 호출 후 화면 갱신
- 타이머, 애니메이션, 상태 관리

### 4.2 필수 JavaScript 코드 예시
```html
<button id="helloBtn">클릭</button>
<p id="result"></p>

<script>
  const button = document.getElementById("helloBtn");
  const result = document.getElementById("result");

  button.addEventListener("click", () => {
    result.textContent = "안녕하세요! JavaScript가 DOM을 변경했습니다.";
  });
</script>
```

### 4.3 JavaScript 실행 원리(기초)
1. 브라우저가 HTML 파싱 후 DOM(Document Object Model) 생성
2. CSS 파싱 후 CSSOM 생성
3. JavaScript 엔진이 스크립트를 실행
4. 이벤트(클릭/입력)가 발생하면 등록된 함수(콜백) 실행
5. DOM 변경 시 브라우저가 다시 렌더링하여 화면 갱신

> [!TIP]
> HTML은 구조, CSS는 디자인, JavaScript는 동작을 담당한다. 세 가지를 분리해서 작성하면 유지보수가 쉬워진다.

## 5. 통합 필수 코드 안내 (한 파일 예시)
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Web Basics</title>
  <style>
    body { font-family: sans-serif; padding: 20px; }
    .box { border: 1px solid #ddd; padding: 12px; border-radius: 8px; }
  </style>
</head>
<body>
  <div class="box">
    <h1>HTML + CSS + JS</h1>
    <button id="btn">메시지 보기</button>
    <p id="msg"></p>
  </div>

  <script>
    document.getElementById("btn").addEventListener("click", function () {
      document.getElementById("msg").textContent = "웹의 3요소가 함께 동작합니다.";
    });
  </script>
</body>
</html>
```

## 실습 미션
1. 자기소개 HTML 페이지를 작성한다.
2. CSS로 카드 UI를 만들고 색상/간격/폰트를 조정한다.
3. 버튼 클릭 시 문구가 바뀌는 JavaScript 기능을 추가한다.
4. 입력 폼에서 이메일 형식을 검사하는 간단한 검증 로직을 구현한다.

## 정리
이번 주차에서 HTML 구조, CSS 스타일링, JavaScript 동작 원리를 연결해 웹 프론트엔드의 핵심 3요소를 이해했다.
