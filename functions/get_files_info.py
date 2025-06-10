from pathlib import Path

def get_files_info(working_directory, directory=None):

    if not directory or not Path(Path(working_directory)/directory).is_dir():
        return f'Error: "{directory}" is not a directory'

    try:
        abs_working = Path(working_directory).resolve(strict=True)
        abs_dir = Path(Path(working_directory)/directory).resolve(strict=True)

        if not abs_dir.is_relative_to(abs_working):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        output = [f'- {item.name}: file_size={item.stat().st_size} bytes, is_dir={item.is_dir()}' for item in Path.iterdir(abs_dir)]
        return "\n".join(output)

    except Exception as e:
         return f"Error: An unexpected error occurred: {e}"
