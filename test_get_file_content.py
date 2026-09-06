from functions.get_file_content import get_file_content
from config import MAX_CHARS

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result = get_file_content("calculator", "main.py")
if len(result) > MAX_CHARS:
    print(f"main.py length: {len(result)}")
    print(f"main.py truncated: {'truncated' in result}")
print(result)

result = get_file_content("calculator", "pkg/calculator.py")
if len(result) > MAX_CHARS:
    print(f"main.py length: {len(result)}")
    print(f"main.py truncated: {'truncated' in result}")
print(result)

result = get_file_content("calculator", "/bin/cat")
if len(result) > MAX_CHARS:
    print(f"main.py length: {len(result)}")
    print(f"main.py truncated: {'truncated' in result}")
print(result)

result = get_file_content("calculator", "pkg/does_not_exist.py")
if len(result) > MAX_CHARS:
    print(f"main.py length: {len(result)}")
    print(f"main.py truncated: {'truncated' in result}")
print(result)