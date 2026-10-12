from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file
load_dotenv()

# Create a connection to OpenAI
client = OpenAI()

# Send our first message to the AI

response = client.responses.create(
    model="gpt-6-luna",
    instructions="""
    You are the AI assistant for Capital Craft Advisors.

    The company provides these services:
    - Real Estate Funding
    - Home Loans
    - Business Loans
    - Mortgage Loans (LAP)
    - Lease Rental Discounting (LRD)

    Answer questions politely and clearly.
    Only share information provided in your instructions.
    Do not invent interest rates, eligibility rules, loan approvals,
    fees, or financial terms.
    If you do not know an answer, say that a company representative
    can provide the details.
    """,
    input="What services does Capital Craft Advisors provide?"
)

print(response.output_text)


