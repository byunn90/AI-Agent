import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    lines = []
    for item in os.listdir(full_path):
        item_path = os.path.join(full_path, item)
        size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(lines)

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    lines = []
    for item in os.listdir(full_path):
        item_path = os.path.join(full_path, item)
        size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
    return "\n".join(lines)


    

