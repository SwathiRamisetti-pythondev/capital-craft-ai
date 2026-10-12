
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from .env
load_dotenv()

# Connect to OpenAI
client = OpenAI()

# Instructions for our company assistant
instructions = """
You are the AI assistant for Capital Craft Advisors.

The company provides these services:
- Real Estate Funding
- Home Loans
- Business Loans
- Mortgage Loans (LAP)
- Lease Rental Discounting (LRD)

Answer politely and clearly.
Do not invent interest rates, eligibility rules, fees, or loan approvals.
If you do not know an answer, recommend contacting a company representative.
"""

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
        instructions=instructions,
        input=question
    )

    print("\nCapital Craft AI:", response.output_text)
