import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    path_size = os.path.getsize(full_path)

    is_dir = os.path.isdir(full_path)
    lines = []

    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    for i in os.listdir(full_path):
        print("test", i)
        lines.append(i)
        
    get_files = os.listdir(full_path)
    print("".join(lines))
    print(path_size)
    print(f"file_size: {path_size} bytes, is_dir={is_dir}")
    return full_path, get_files

print(get_files_info(".", "functions"))
