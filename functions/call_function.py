from functions.get_files_info import get_files_info
from functions.run_python import run_python_file
from functions.write_file import write_file
from functions.get_file_content import get_file_content

from google.genai import types

def call_function(function_call, verbose=False):
    can_call = {
        "get_files_info" : get_files_info,
        "run_python_file" : run_python_file,
        "write_file" : write_file,
        "get_file_content" : get_file_content,
    }
    if function_call.name not in can_call:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={"error": f"Unknown function: {function_call.name}"},
                )
            ],
        )

    print(f" - Calling function: {function_call.name}" + f"({function_call.args})" if verbose else "")
    results = can_call[function_call.name]("./calculator", **function_call.args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call.name,
                response={"result": results},
            )
        ],
    )
