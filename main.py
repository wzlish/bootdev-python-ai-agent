import os
from dotenv import load_dotenv
from google import genai

from exceptions import APIKeyError, NoMetadataError

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "YOURAPIKEY":
        raise APIKeyError("GEMINI_API_KEY not set in .env")

    client = genai.Client(api_key=api_key)

    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,
    )
    if response.usage_metadata:
        print("Response: ", response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count} | Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        raise NoMetadataError("No usage_metadata returned with the client response, something went wrong.")


if __name__ == "__main__":
    main()
