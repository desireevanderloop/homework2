import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# Configurable system instruction
SYSTEM_PROMPT = """You are a communications assistant for a university office. 
Summarize the following text in exactly 3 bullet points. 
Each bullet point should be one complete sentence that captures a key idea."""

# Configurable input text
INPUT_TEXT = """
Johns Hopkins University is a private research university in Baltimore, Maryland. 
Founded in 1876, it was the first research university in the United States. 
The university was named after its first benefactor, the philanthropist Johns Hopkins. 
It consistently ranks among the top universities in the world and is known for its 
medical school, public health programs, and research output. The university has 
produced numerous Nobel laureates, National Academy members, and Rhodes Scholars.
"""

def summarize(text):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Text: {text}"
            }
        ]
    )
    return message.content[0].text

def main():
    print("=" * 50)
    print("AI Text Summarization Workflow")
    print("=" * 50)
    print("\nInput Text:")
    print(INPUT_TEXT)
    print("\nSummary:")
    print("-" * 50)
    
    result = summarize(INPUT_TEXT)
    print(result)
    
    print("-" * 50)
    
    # Save output to file
    with open("output.txt", "w") as f:
        f.write("INPUT:\n")
        f.write(INPUT_TEXT)
        f.write("\nSUMMARY:\n")
        f.write(result)
    
    print("\nOutput saved to output.txt")

if __name__ == "__main__":
    main()