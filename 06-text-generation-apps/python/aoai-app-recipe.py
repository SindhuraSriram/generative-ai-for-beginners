from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI client
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

# Use gpt-3.5-turbo or gpt-4 depending on your access
model = "gpt-3.5-turbo"

# Take user input
no_recipes = input("No of recipes (for example, 5): ")
ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")
filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

# First prompt: generate recipes
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}:"
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=600,
    temperature=0.1
)

print("Recipes:")
print(completion.choices[0].message.content)

# Use result in a new prompt
old_prompt_result = completion.choices[0].message.content
prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "

new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
messages = [{"role": "user", "content": new_prompt}]

completion = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=600,
    temperature=0
)

print("\n===== Shopping List =====")
print(completion.choices[0].message