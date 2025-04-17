# 📄 Day7.5 리포트: 상태 전이 시퀀스 구성

---

## ✅ 학습 주제

- 사용자별 행동 흐름에서 **중복된 상태 제거**
- **상태 전이 발생 시점만 기록**
- 중첩 없이 단일 딕셔너리 기반 상태 기록

---

## 📌 핵심 개념 요약

| 항목 | 설명 |
|------|------|
| 상태 전이란? | 이전 상태와 다를 때 발생하는 행동 변화 |
| `last_state[user]` | 사용자별 마지막 상태를 저장하여 비교 |
| `defaultdict(list)` | 사용자별 상태 리스트 자동 초기화 |
| 순서 유지 | 입력된 로그 순서대로 처리하며 전이 여부 판단 |
| `dict()` 변환 | 결과 출력 시 실무 가독성을 위해 변환 |

---

## ✅ 제출 코드

```python
from collections import defaultdict
from pprint import pprint

logs = [
    ("2025-04-05", "kim", "visit"),
    ("2025-04-05", "kim", "visit"),
    ("2025-04-05", "kim", "cart"),
    ("2025-04-05", "kim", "cart"),
    ("2025-04-05", "kim", "buy"),
    ("2025-04-05", "lee", "visit"),
    ("2025-04-05", "lee", "buy"),
    ("2025-04-06", "lee", "buy")
]

users_states = defaultdict(list)
last_state = {}

for _, user, state in logs:
    if not user in last_state or last_state[user] != state:
        users_states[user].append(state)
        last_state[user] = state

pprint(dict(users_states))
```

---

## ✅ 출력 결과 예시

```python
{
  "kim": ["visit", "cart", "buy"],
  "lee": ["visit", "buy"]
}
```

---

## ✅ 평가 요약

| 항목 | 평가 | 설명 |
|------|------|------|
| 구조 설계 | ⭐⭐⭐⭐⭐ | 상태 전이 흐름을 정확하게 구현 |
| 로직 흐름 | ⭐⭐⭐⭐⭐ | 전이 여부 판단 조건 명확 |
| 실무 적용성 | ⭐⭐⭐⭐⭐ | 퍼널 분석, 이탈 추적, 전환 시점 분석에 바로 사용 가능 |
| 출력 포맷 | ⭐⭐⭐⭐☆ | dict 변환 + pprint 구조 적용 |
| 변수 흐름 | ⭐⭐⭐⭐☆ | 의미 중심의 네이밍 시도 확인됨 |

---

## 🧠 배운 점 요약

- 단순 중복 제거와 전이 판단은 전혀 다른 문제임을 명확히 체득
- 사용자별로 현재 상태와 마지막 상태를 비교하여 설계해야 전이 여부를 판단 가능
- 실무 로그에서 가장 많이 쓰이는 “상태 변화 시점 기록 구조”를 직접 구현함

---

## 🔁 다음 연결 흐름 (보류 중)

| Day | 주제 |
|-----|------|
| Day8 | Pandas + groupby + shift()로 상태 전이 자동화 |
| Day8.5 | 시간 간격 분석 + 행동 간 이탈 계산 등 |

---
