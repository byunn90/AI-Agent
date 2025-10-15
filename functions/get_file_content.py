import os

def get_file_content(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    # keep inside sandbox
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # must be a real file
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    try:
        with open(full_path, "r") as f:
            content = f.read(MAX_CHARS)
            # if there’s more data, append the truncation notice
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {e}"


