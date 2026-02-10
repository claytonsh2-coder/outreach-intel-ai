from dotenv import load_dotenv
import os
from typing import Optional

# Load .env file into environment (no-op if .env missing)
load_dotenv()


def get_api_key(env_var: str = "OPENAI_API_KEY") -> Optional[str]:
    """Return the API key stored in environment variable `env_var`.

    - Do NOT hard-code secret values here. Put the actual key in a `.env` file
      or your OS environment and reference it by name (default: `OPENAI_API_KEY`).
    - Returns `None` if the variable is not set.
    """
    return os.getenv(env_var)


def require_api_key(env_var: str = "OPENAI_API_KEY") -> str:
    """Return the API key, or raise a clear error if missing."""
    key = get_api_key(env_var)
    if not key:
        raise EnvironmentError(
            f"Environment variable {env_var} is not set. Copy .env.example -> .env and set the value."
        )
    return key
