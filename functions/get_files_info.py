import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    lines = []

    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    for item in os.listdir(full_path):
        item_path = os.path.join(full_path, item)
        size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

    
    return "\n".join(lines)

print(get_files_info(".", "functions"))



def get_file_content(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    list = []

    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    MAX_CHARS = 10000

    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)


    

    

print(get_file_content(".", "functions"))
