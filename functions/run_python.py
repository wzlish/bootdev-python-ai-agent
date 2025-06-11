from pathlib import Path
import subprocess

def run_python_file(working_directory, file_path):

    try:
        abs_working = Path(working_directory).resolve(strict=True)
        abs_file = Path(Path(working_directory)/file_path).resolve(strict=True)

        if not abs_file.is_relative_to(abs_working):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not abs_file.is_file():
           return f'Error: File "{file_path}" not found.'

        if not abs_file.suffix == ".py":
            return f'Error: "{file_path}" is not a Python file.'

        try:
            proc = subprocess.run(["python3", abs_file], cwd=abs_working, timeout=30, capture_output=True, encoding='utf-8')

            output = []
            if len(proc.stdout)>0:
                output.append(f'STDOUT: {proc.stdout}')

            if len(proc.stderr)>0:
                output.append(f'STDERR: {proc.stderr}')

            if proc.returncode>0:
                output.append(f'Process exited with code {proc.returncode}')

            if len(proc.stdout) == len(proc.stderr) == 0:
                output.append("No output produced.")

            return "\n".join(output)

        except Exception as e:
              return f"Error: executing Python file: {e}"
    except Exception as e:
         return f"Error: An unexpected error occurred: {e}"
