import os

import re


def extract_day_number(path):
    match = re.search(r"day(\d+(?:\.\d+)?)", path)
    if match:
        return float(match.group(1))
    return float("inf")


def find_day_markdown_files():
    md_files = []
    for root, dirs, files in os.walk("."):
        # ✅ Checkpoints 폴더는 탐색 대상에서 제거
        dirs[:] = [d for d in dirs if d != ".ipynb_checkpoints"]

        for file in files:
            if file.endswith(".md") and file != "README.md":
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, ".")
                md_files.append(relative_path)
    # return sorted(md_files)
    return sorted(md_files, key=extract_day_number)


def extract_title(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("#"):
                return line.strip().lstrip("#").strip()
    return os.path.basename(file_path)


def generate_toc():
    print("📌 자동 목차 갱신 시작...")
    md_files = find_day_markdown_files()

    if not md_files:
        print("⚠️  Markdown 파일이 발견되지 않았습니다.")
        return

    toc_lines = ["## 📚 목차 (자동 생성)\n"]
    for path in md_files:
        title = extract_title(path)
        toc_lines.append(f"- [{title}]({path})")

    with open("README.md", "r", encoding="utf-8") as f:
        pre = f.read().split("## 📚 목차 (자동 생성)")[0]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(pre.strip() + "\n\n" + "\n".join(toc_lines) + "\n")

    print("✅ 목차가 성공적으로 갱신되었습니다!")


if __name__ == "__main__":
    generate_toc()
