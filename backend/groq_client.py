import os
from dotenv import load_dotenv

load_dotenv()

try:
    from groq import Groq
except ImportError:                       
    raise ImportError(
        "The `groq` package is not installed. "
        "Run `pip install groq` (and add it to requirements.txt/pyproject)."
    )

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

def test_groq():
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": "Explain AI in simple words."}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print(test_groq())