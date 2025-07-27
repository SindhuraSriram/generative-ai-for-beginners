from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Choose model (e.g., gpt-3.5-turbo or gpt-4 if you have access)
model = "gpt-3.5-turbo"

# User input
persona = input("Tell me the historical character you want to be: ")
question = input("Ask your question about the historical character: ")

# Prompt construction
prompt = f"""
You are going to play as a historical character {persona}. 

Whenever certain questions are asked, you need to remember facts about the timelines and incidents and respond with accurate answers only. Don't create content yourself. If you don't know something, say that you don't remember.

Provide answer for the question: {question}
"""

messages = [{"role": "user", "content": prompt}]

# Get response from OpenAI
completion = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0
)

# Print the response
print("\n===== Response =====\n")
print(completion.choices[0].message.content)
