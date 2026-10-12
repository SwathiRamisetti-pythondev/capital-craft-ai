from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file
load_dotenv()

# Create a connection to OpenAI
client = OpenAI()

# Send our first message to the AI
response = client.responses.create(
    model="gpt-6-luna",
    input="Introduce yourself as the AI assistant for Capital Craft Advisors in one sentence."
)

# Display the AI's response
print(response.output_text)