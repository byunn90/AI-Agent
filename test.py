from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print("Result for current directory:")
print(get_files_info("calculator", "."))

print("\nResult for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))

print("\nResult for '/bin' directory:")
print(get_files_info("calculator", "/bin"))

print("\nResult for '../' directory:")
print(get_files_info("calculator", "../"))

print("Result for lorem.txt (should be truncated if >10k):")
out = get_file_content("calculator", "lorem.txt")
print(out)
print("\n--- sanity checks ---")
print("len:", len(out))
print("\nResult for lorem.txt (should be truncated if >10k):")
print("has notice:", '[...File "lorem.txt" truncated at 10000 characters]' in out)

