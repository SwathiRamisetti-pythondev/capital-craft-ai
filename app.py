
import streamlit as st
from lead_form import show_lead_form


from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from your local .env file
load_dotenv()

# Connect to the OpenAI API
client = OpenAI()

# Read the company's information
with open("company_info.txt", "r", encoding="utf-8") as file:
    company_info = file.read()


st.set_page_config(
    page_title="Capital Craft AI",
    page_icon="🏢",
    layout="centered"
)

st.title("Capital Craft AI")
st.subheader("Capital Craft Advisors")

st.write(
    "Welcome! I can help answer questions about "
    "our company services."
)

st.info(
    "Ask about Real Estate Funding, Home Loans, "
    "Business Loans, Mortgage Loans (LAP), or "
    "Lease Rental Discounting (LRD)."
)

st.caption("Your AI assistant for Capital Craft Advisors")


# Create a chat area for visitors
st.subheader("Chat with Capital Craft AI")

# Remember the conversation while the website is open
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Let the visitor type a question
question = st.chat_input("Ask us about our services...")

if question:
    # Display and save the visitor's question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    # Ask the AI to answer using company information
    with st.spinner("Capital Craft AI is thinking..."):
        response = client.responses.create(
            model="gpt-6-luna",
            instructions=(
                "You are Capital Craft AI, a helpful assistant for "
                "Capital Craft Advisors. Use the company information "
                "below to answer questions clearly and accurately. "
                "Do not invent interest rates, fees, eligibility rules, "
                "loan approvals, or financial terms. If you do not "
                "know an answer, recommend contacting a company representative.\n\n"
                + company_info
            ),
            input=question,
        )

    answer = response.output_text

    # Display and save the AI's answer
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)


# Display the callback request form
show_lead_form()
