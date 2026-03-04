# Week 03 — Flask 서버 기초 확장

## 학습 목표
- HTTP 요청/응답의 기본 구조를 설명할 수 있다.
- Flask 라우팅으로 URL별 기능을 분리할 수 있다.
- 템플릿 렌더링으로 동적 웹 페이지를 만들 수 있다.

---

## 1. 웹 서버란 무엇인가?

웹 서버는 사용자의 요청(Request)을 받고, 결과(Response)를 돌려주는 프로그램입니다.
Flask는 Python으로 이 과정을 쉽게 구현하게 해주는 프레임워크입니다.

---

## 2. GET과 POST

- GET: 주로 데이터 조회
- POST: 주로 데이터 생성/전송

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"
```

---

## 3. 라우팅과 URL 파라미터

```python
@app.route('/user/<username>')
def user_profile(username):
    return f"{username}님의 프로필 페이지"
```

라우팅은 URL과 함수를 연결하는 핵심 기능입니다.

---

## 4. 템플릿 렌더링

```python
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)
```

템플릿을 쓰면 HTML과 Python 로직을 분리할 수 있어 유지보수가 쉬워집니다.

---

## 5. 미니 프로젝트: 할 일 목록 서버

- `/tasks`에서 목록 조회(GET)
- `/tasks`로 신규 할 일 등록(POST)

이 구조를 통해 REST API 설계의 기본 감각을 익힐 수 있습니다.

---

## 정리
- 웹은 요청/응답으로 동작한다.
- Flask 라우팅은 기능 분리의 시작점이다.
- 템플릿은 동적 화면 구성의 핵심이다.
