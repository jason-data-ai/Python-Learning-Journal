# 📄 Day7 리포트: 사용자 상태 시퀀스 구조

---

## ✅ 개요

| 항목 | 내용 |
|------|------|
| 📌 학습 주제 | 사용자별 상태 누적 구조 설계 (`defaultdict(list)`) |
| 🎯 학습 목표 | 중첩 딕셔너리 없이, 단일 사용자 행동 시퀀스를 구성하고 출력 |
| 🧠 핵심 개념 | 리스트 누적, 반복문, 자동 초기화 구조 |
| 🔧 사용 기술 | `defaultdict(list)` + 루프 누적 + 출력 포맷 (`pprint`) |

---

## 📘 실전 시나리오

```python
logs = [
    ("2025-04-05", "kim", "visit"),
    ("2025-04-05", "kim", "cart"),
    ("2025-04-05", "kim", "buy"),
    ...
]
```

> → 사용자별 행동을 시간 흐름대로 **그대로 누적하는 구조**

---

## 🧠 구조 설명

```python
from collections import defaultdict
from pprint import pprint

user_logs = defaultdict(list)

for _, name, action in logs:
    user_logs[name].append(action)

pprint(dict(user_logs))
```

- 사용자별 리스트를 자동으로 생성 (`defaultdict(list)`)
- 로그 순서대로 append
- 출력 시 `dict()`로 변환하여 깔끔한 구조 생성

---

## ✅ 출력 예시

```python
{
  "kim": ["visit", "cart", "buy", "visit", "cart"],
  "lee": ["visit", "buy", "visit", "cart", "buy"]
}
```

---

## ✅ 평가 요약

| 항목 | 평가 | 설명 |
|------|------|------|
| 구조 구성 | ⭐⭐⭐⭐⭐ | 매우 간결하고 정확 |
| 로직 흐름 | ⭐⭐⭐⭐⭐ | 반복문 구성 및 append 흐름 적절 |
| 실무 적용성 | ⭐⭐⭐⭐☆ | 분석용 로그 구조로 안정적, 날짜 분기 없다는 점만 명확히 인식 필요 |
| pprint 활용 | ⭐⭐⭐⭐⭐ | 출력 구조 정리까지 훌륭 |
| 변수 명 가독성 | ⭐⭐⭐⭐☆ | `user_logs` → 추후 중첩 구조와 구분되면 더 좋음 |

---

## 📌 배운 점 요약

- `defaultdict(list)`는 가장 기본적이면서도 강력한 누적형 구조
- 로그처럼 **시간 순서대로 쌓이는 데이터**는 리스트 형태로 그대로 저장하는 게 핵심
- `pprint()`와 `dict()` 변환은 **실전에서 가장 많이 쓰는 출력 조합**

---

## 🔄 코드 스타일 개선 (무시 변수 `_`)

```python
for _, name, action in logs:
    ...
```

- `date`가 실제로 사용되지 않을 경우, `_`로 명확하게 무시 의도 표현
- 가독성 + 유지보수성 향상
- `log[1]`, `log[2]` 방식보다 훨씬 선호됨 (PEP8 권장)

---

## 🔁 다음 연결 흐름

| Day | 연결 개념 |
|-----|-----------|
| Day6 | 중첩 구조 (user → date → action) |
| **Day7.5** | 상태 전이 시퀀스 (중복 제거 → 행동 전환만 추출) |
| Day8 | Pandas로 시퀀스/그룹 구조를 DataFrame에서 처리 |

---
