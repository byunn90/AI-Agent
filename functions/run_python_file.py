import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    timer = 30
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
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
        timeout=timer,                      
        cwd=working_directory            
        )
        out = completed.stdout
        er  = completed.stderr
        code = completed.returncode
        if out == "" and er == "":
            return "No output produced"

        if completed.returncode != 0:
            return "Process exited with code f{code}"
        else:
            return f"STDOUT: {out}\nSTDERR: {er}"

    except Exception as e:
        return f"Error: executing Python file: {e}"
        
 




