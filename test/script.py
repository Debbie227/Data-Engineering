from pathlib import Path

currentDir = Path.cwd()
currentFile = Path(__file__).name

print(f"files in {currentDir}:")

for filepath in currentDir.iterdir():
    if filepath.name == currentFile:
        continue

    print(f" - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")
