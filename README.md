# 🧠 Python 학습 저널

본 저장소는 Python 기초부터 실습까지의 학습 여정을 기록한 포트폴리오입니다.
각 Day는 폴더로 분리되어 있으며, 실습, 요약, 테스트 결과가 포함되어 있습니다.

## 📚 목차 (자동 생성)

-   [Day 1 - Number Operations in Python](01_python_math_basics/day1_number_operations.md)
-   [📘 Day 2 - Conditionals (if / elif / else) & Logic Operators](day2_conditionals/day2_conditionals.md)
-   [🔁 Day 3 – 반복문 완전 체득 정리](day3_Loops/Day3_loops_summary.md)
-   [📚 Day 4 – 함수 완전 체득 정리](day4_Function/Day4_functions_summary.md)
-   [📄 Day6 리포트: 중첩 딕셔너리 구조 설계](day6_dictionary/day6_dictionary.md)
-   [📄 Day7 리포트: 사용자 상태 시퀀스 구조](day7_user_state/day7_user_state.md)
-   [📄 Day7.5 리포트: 상태 전이 시퀀스 구성](day7.5_state_transition/day7.5_state_transition.md)

## Python 환경 설정

이 프로젝트는 [pyenv](https://github.com/pyenv/pyenv) 및 [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)를 사용하여  
Python 버전과 가상환경을 관리합니다.

필요한 Python 버전과 가상환경 이름은 `.python-version` 파일에 정의되어 있습니다.  
`pyenv`가 설치되어 있다면, 해당 디렉토리로 이동할 때 자동으로 환경이 활성화됩니다.

This project uses [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) for Python version and environment management.

The required Python version and virtual environment are defined in the `.python-version` file.  
If you have pyenv properly installed, the environment will be automatically activated when you enter this directory.

### 초기 설정 방법 (최초 1회만 실행)

```bash
# 필요한 Python 버전 설치 (예: 3.12.2)
# Install the required Python version
pyenv install 3.12.2

# 동일한 이름의 가상환경 생성 (예: pyenv-venv)
# Create the virtual environment if not already present
pyenv virtualenv 3.12.2 pyenv-venv
```

그 다음, 프로젝트 디렉토리로 이동하면 자동으로 환경이 활성화됩니다:

```bash
cd path/to/project
# .python-version 파일에 따라 pyenv가 자동으로 가상환경 activate
# Environment auto-activates via .python-version
```
