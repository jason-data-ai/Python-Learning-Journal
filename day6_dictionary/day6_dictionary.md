# 📄 Day6 리포트: 중첩 딕셔너리 구조 설계

---

## ✅ 학습 주제

- 중첩 딕셔너리 구조 이해 및 설계
- `defaultdict` vs `.setdefault()` 비교
- 상태 저장 구조 설계: 날짜 → 사용자 → 행동

---

## 📌 핵심 개념 요약

| 항목 | 설명 |
|------|------|
| `defaultdict(list)` | 키가 없을 경우 자동으로 빈 리스트 생성 |
| `.setdefault(key, [])` | 키가 없을 경우 해당 키에 빈 리스트 삽입 후 append |
| `defaultdict(dict)` | 중첩 딕셔너리 기본 구조 |
| 상태 누적 구조 | 날짜 → 사용자 → 행동 시퀀스를 중첩 딕셔너리로 표현 |

---

## 🧠 학습 코드 흐름 요약

```python
from collections import defaultdict

logs = [
    ("2025-04-01", "kim", "visit"),
    ("2025-04-01", "lee", "visit"),
    ("2025-04-01", "kim", "cart"),
    ("2025-04-01", "kim", "buy"),
    ("2025-04-02", "lee", "visit"),
    ("2025-04-02", "choi", "visit"),
    ("2025-04-02", "choi", "cart")
]

user_logs = defaultdict(dict)

for log in logs:
    if not log[1] in user_logs:
        user_logs[log[1]].setdefault(log[0], []).append(log[2])
    elif not user_logs[log[1]].get(log[0]):
        user_logs[log[1]].setdefault(log[0], []).append(log[2])
    else:
        user_logs[log[1]][log[0]].append(log[2])
```

---

## ✅ 평가 요약

| 항목 | 평가 | 설명 |
|------|------|------|
| 구조 설계 | ⭐⭐⭐⭐☆ | 중첩 구조 흐름 구성 정확, 조건 분기 중복 약간 있음 |
| `.setdefault()` 이해 | ⭐⭐⭐⭐⭐ | 리스트 초기화 목적에 맞게 정확히 사용 |
| defaultdict(dict) | ⭐⭐⭐⭐☆ | 활용 목적에 부합, 단 lambda 구조로 개선 여지 있음 |
| 조건 흐름 | ⭐⭐⭐⭐☆ | 중복 if → elif 최적화 가능, 설계적 의도는 명확 |

---

## 📘 리포트 요약

- 중첩 딕셔너리의 구조와 흐름을 체득한 첫 번째 단계
- `user → date → action list`의 구조를 수작업으로 설계
- 조건 분기를 직접 구현함으로써 **자동화 설계 이전의 기반 학습 완성**
- 다음 학습의 lambda + defaultdict 구조를 위한 핵심 전제 학습

---

## 🔁 다음 학습 계획

| Day | 주제 |
|-----|------|
| **Day6_lambda** | `defaultdict(lambda: defaultdict(list))` 구조로 자동화 설계 |
| Day7 | 사용자별 상태 시퀀스를 단일 리스트로 구성 (`defaultdict(list)`) |
| Day7.5 | 상태 전이 흐름 구성으로 확장 예정 |

---

---

## 📚 딕셔너리 핵심 개념 정리 (추가 확장)

---

### 🔹 기본 구조

```python
d = {"a": 1, "b": 2}
```

- 키는 고유해야 하며, 리스트/딕셔너리와 달리 인덱스가 없음
- 순회는 기본적으로 키 기준

---

### 🔹 주요 메서드 요약

| 메서드 | 설명 | 예시 |
|--------|------|------|
| `d.keys()` | 키 목록 반환 | `dict_keys(['a', 'b'])` |
| `d.values()` | 값 목록 반환 | `dict_values([1, 2])` |
| `d.items()` | (키, 값) 쌍 반환 | `[('a', 1), ('b', 2)]` |
| `d.get(k)` | 키 없을 경우 None 반환 | `d.get('c') → None` |
| `d[k]` | 키 없을 경우 에러 | `d['c'] → KeyError` |
| `d.setdefault(k, [])` | 키 없으면 값 초기화 후 반환 | `d.setdefault('x', []).append(1)` |
| `d.update({})` | 딕셔너리 병합 | `d.update({'x': 3})` |
| `del d[k]` | 키 삭제 | `del d['a']` |

---

### 🔹 딕셔너리 컴프리헨션

```python
squared = {x: x**2 for x in range(5)}
```

- 조건 포함도 가능: `{x: x for x in nums if x > 0}`

---

### 🔹 중첩 딕셔너리 패턴

```python
from collections import defaultdict

d = defaultdict(lambda: defaultdict(list))
d["kim"]["2025-04-01"].append("visit")
```

- 자동 초기화의 궁극체
- `.setdefault()`보다 더 깔끔한 패턴
- 단, 무조건 lambda로 감싸야 안전 (shared 객체 문제 방지)

---

### 🔹 반복문 패턴

```python
for k, v in d.items():
    print(k, v)
```

- `.items()`는 실무에서 거의 모든 루프의 기본
- `.values()`만 반복할 때는 키가 필요 없을 때만 사용

---

### 🔹 주의 사항

- `dict()`는 클래스, `defaultdict()`도 클래스
- `list`는 callable이므로 `defaultdict(list)`처럼 쓸 수 있음
- `defaultdict(defaultdict(list))`는 객체가 즉시 생성돼 **모든 키가 같은 객체를 참조함**
    → 반드시 lambda로 감싸야 각각의 독립된 객체 생성 가능

---

