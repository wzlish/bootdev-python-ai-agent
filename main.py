import os
import sys
import argparse

from google import genai
from google.genai import types

from functions.call_function import call_function

from functions.schema import schema_get_files_info, schema_run_python_file, schema_write_file, schema_get_file_content

from exceptions import APIKeyError, NoMetadataError, NoContentFunctionResponse
from config import init_config
from importlib.resources import contents

def main():

    config = init_config()

    api_key = config.get("GEMINI_API_KEY", "")
    if not api_key or api_key == "YOURAPIKEY":
        raise APIKeyError("GEMINI_API_KEY not set in .env")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output")
    parser.add_argument('prompt', help="Your prompt text")

    args = parser.parse_args()

    if not args.prompt:
        parser.print_help()
        sys.exit(1)

    prompt = str.strip(args.prompt)
    if prompt=="":
        print("Your prompt can't just be whitespace.")
        sys.exit(1)

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_run_python_file,
            schema_write_file,
            schema_get_file_content,
        ]
    )

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    response = False
    for i in range(20):

        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig( system_instruction=config.get("GEMINI_SYSTEM_PROMPT", ""),
                                                tools=[available_functions],
            ),
        )

        if not response.usage_metadata:
            raise NoMetadataError("No usage_metadata returned with the client response, something went wrong.")

        response_text = ""
        if response and response.candidates:
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)
                    if candidate.content.parts:
                        response_text += "".join([part.text for part in candidate.content.parts if part.text])

        if response.function_calls and response.function_calls[0]:
            func = response.function_calls[0]
            result = call_function(func, args.verbose)
            if not result.parts or not result.parts[0].function_response or not result.parts[0].function_response.response:
                raise NoContentFunctionResponse("No result.parts[0].function_response.response returned.")
            if args.verbose:
                print(f"-> {result.parts[0].function_response.response}")
            messages.append(result)
            print(response_text)
        else:
            if response:
                if args.verbose:
                    print(f"User prompt: {prompt}")
                    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
                print(response_text)
            break


if __name__ == "__main__":
    main()
