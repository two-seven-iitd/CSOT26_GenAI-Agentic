import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

def call_model(prompt: str) -> str:
    """
    Make a single chat completion call.
    Print the full response object first and understand its structure.
    Then return just the assistant's text.
    """
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who gives short, direct answers."},
            {"role": "user", "content": prompt}
        ],
    )
    print("\n--- FULL RESPONSE OBJECT ---")
    print(response)
    print("\n--- CHOICES ---")
    print(response.choices)
    print("\n--- USAGE (tokens) ---")
    print(response.usage)
    print("----------------------------\n")
    return response.choices[0].message.content

if __name__ == "__main__":
    print(call_model("What is the capital of Australia?"))
