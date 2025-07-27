from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Model choice — use "gpt-3.5-turbo" or "gpt-4" depending on access
model = "gpt-3.5-turbo"

# Ask user for question
question = input("Ask your questions on Python language to your study buddy: ")

# Prompt format
prompt = f"""
You are an expert on the Python language.

Whenever certain questions are asked, you need to provide responses in the following format:

- Concept
- Example code showing the concept implementation
- Explanation of the example and how the concept is implemented to help the user understand better.

Provide answer for the question: {question}
"""

# Construct message
messages = [{"role": "user", "content": prompt}]

# Generate response
completion = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0.3
)

# Output result
print("\n===== Python Study Buddy Answer =====\n")
print(completion.choices[0].message.content)
