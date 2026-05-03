import os

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv()

    api_key = os.getenv("LLM_API_KEY")
    model = os.getenv("LLM_MODEL", "gpt-4.1-mini")
    base_url = os.getenv("LLM_BASE_URL")

    if not api_key:
        raise SystemExit("Missing LLM_API_KEY. Add it to your .env file.")

    # base_url is optional; useful for OpenAI-compatible providers.
    client = OpenAI(api_key=api_key, base_url=base_url)

    response = client.responses.create(
        model=model,
        input="Give me one short practical tip for learning LLM APIs.",
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
