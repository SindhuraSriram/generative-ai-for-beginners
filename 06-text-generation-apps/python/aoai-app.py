# pylint: disable=all
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Use model name directly (e.g., "gpt-3.5-turbo" or "gpt-4")
model = "gpt-3.5-turbo"

# Define the prompt
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]

# Make completion
completion = client.chat.completions.create(
    model=model,
    messages=messages
)

# Print response
print(completion.choices[0].message.content)