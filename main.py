
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from .env
load_dotenv()

# Connect to OpenAI
client = OpenAI()

# Instructions for our company assistant

# Read company information from the text file
with open("company_info.txt", "r", encoding="utf-8") as file:
    company_info = file.read()


# Keep asking questions until the user exits
while True:
    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Capital Craft AI: Goodbye!")
        break

    if not question.strip():
        continue

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=company_info,
        input=question
    )

    print("\nCapital Craft AI:", response.output_text)
