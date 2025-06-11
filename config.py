import os
from dotenv import load_dotenv

def init_config():
    config = {
        "MAX_CHARS": 10000,
        "GEMINI_SYSTEM_PROMPT" : """
        You are a helpful AI coding agent called Nuts who is also a wild sorcerer squirrel. You should reply in character, but the character replies should not impact code. You make the occasional snide remarks about bear wizards.

        When the user asks a question or makes a request, make a function call plan. You can perform the following operations:
        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """,
    }
    config["GEMINI_API_KEY"] = "" # Note: Should only ever be set in .env
    load_dotenv()
    for key, default_value in config.items():
        env_var = os.environ.get(key)

        if env_var is not None:
            target_type = type(default_value)
            try:
                if target_type is bool:
                    config[key] = env_var.lower() in ('true', '1', 't', 'y', 'yes')
                elif target_type is list:
                    config[key] = [item.strip() for item in env_var.split(',')]
                elif target_type is tuple:
                    config[key] = tuple(item.strip() for item in env_var.split(','))
                else:
                    config[key] = target_type(env_var)
            except ValueError:
                print(f"Error: Could not cast environment variable '{key}={env_var}' to type {target_type}. Using default value.")

    return config
