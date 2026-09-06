from functions.run_python_file import run_python_file

def print_func(dir, file, args=None):
    print(run_python_file(dir, file, args))
    print("*" * 40)

print_func("calculator", "main.py")
print_func("calculator", "main.py", ["3 + 5"])
print_func("calculator", "tests.py")
print_func("calculator", "../main.py")
print_func("calculator", "nonexistent.py")
print_func("calculator", "lorem.txt")