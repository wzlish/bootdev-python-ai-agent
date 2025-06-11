import os
import sys
import argparse

from google import genai
from google.genai import types

from exceptions import APIKeyError, NoMetadataError
from config import init_config

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

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=config.get("GEMINI_SYSTEM_PROMPT", "")),
    )
    if not response.usage_metadata:
        raise NoMetadataError("No usage_metadata returned with the client response, something went wrong.")

    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print("Response: ", response.text)
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        return

    print(response.text)



if __name__ == "__main__":
    main()
