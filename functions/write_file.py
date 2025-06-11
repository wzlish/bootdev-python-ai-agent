from pathlib import Path

def write_file(working_directory, file_path, content):

    try:
        abs_working = Path(working_directory).resolve(strict=True)
        abs_file = Path(Path(working_directory)/file_path).resolve(strict=False)

        if not abs_file.is_relative_to(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        abs_file.parent.mkdir(parents=True, exist_ok=True)


        with open(abs_file, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
         return f"Error: An unexpected error occurred: {e}"
