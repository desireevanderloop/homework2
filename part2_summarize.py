import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

text = """
Johns Hopkins University is a private research university in Baltimore, Maryland. 
Founded in 1876, it was the first research university in the United States. 
The university was named after its first benefactor, the philanthropist Johns Hopkins. 
It consistently ranks among the top universities in the world and is known for its 
medical school, public health programs, and research output. The university has 
produced numerous Nobel laureates, National Academy members, and Rhodes Scholars.
"""

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=512,
    messages=[
        {
            "role": "user",
            "content": f"Please summarize the following text in 3 bullet points:\n\n{text}"
        }
    ]
)

print(message.content[0].text)