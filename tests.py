from functions.get_file_content import get_file_content

print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))              # should be Error:
print(get_file_content("calculator", "pkg/does_not_exist.py")) # should be Error:
print(get_file_content("calculator", "/home/kayhan/projects/ai-agent/calculator/lorem.txt")) ## Working


