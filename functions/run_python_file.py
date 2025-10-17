import os

def run_python_file(working_directory, file_path, args=[]):
    timer = 30
    full_path = abspath.os.path(join.os.path(working_directory, file))

    if not full_path.startswith(abspath.os.path(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        completed = subprocess.run(
        ["python3", full_path, *args],   
        capture_output=True,             
        text=True,                      
        timeout=30,                      
        cwd=working_directory            
        )
        print(completed.stdout)
        print(completed.stderr)
        print(returncode)
    except Exception as e:
        return f"Error: {e}"
print(run_python_file)
 




