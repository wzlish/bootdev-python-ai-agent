from pathlib import Path
from config import init_config

def get_file_content(working_directory, file_path):

    config = init_config()
    MAX_CHARS = config.get("MAX_CHARS", 10000)

    if not file_path or not Path(Path(working_directory)/file_path).is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        abs_working = Path(working_directory).resolve(strict=True)
        abs_file = Path(Path(working_directory)/file_path).resolve(strict=True)

        if not abs_file.is_relative_to(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        file_content_string = ""
        with open(abs_file, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)

        if len(file_content_string)>MAX_CHARS:
            file_content_string = f'{file_content_string[:-1]}[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
         return f"Error: An unexpected error occurred: {e}"
