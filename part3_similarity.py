import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

sentence1 = "The cat sat on the mat."
sentence2 = "A feline rested on a rug."
sentence3 = "The stock market crashed today."

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    messages=[
        {
            "role": "user",
            "content": f"""Rate the semantic similarity between these sentence pairs on a scale of 0 to 1, and explain your reasoning.

Pair 1:
Sentence A: "{sentence1}"
Sentence B: "{sentence2}"

Pair 2:
Sentence A: "{sentence1}"
Sentence B: "{sentence3}"
"""
        }
    ]
)

print(message.content[0].text)