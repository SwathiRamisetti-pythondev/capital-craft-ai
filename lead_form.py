
import streamlit as st


def show_lead_form():
    st.subheader("Request a Callback")

    st.write(
        "Interested in our services? "
        "Share your contact details and let our team follow up."
    )

    with st.form("lead_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")

        service = st.selectbox(
            "What service are you interested in?",
            [
                "Real Estate Funding",
                "Home Loans",
                "Business Loans",
                "Mortgage Loans (LAP)",
                "Lease Rental Discounting (LRD)",
            ],
        )

        submitted = st.form_submit_button("Request Callback")

        if submitted:
            if not name.strip():
                st.error("Please enter your full name.")
            elif not email.strip():
                st.error("Please enter your email address.")
            elif not phone.strip():
                st.error("Please enter your phone number.")
            else:
                st.success(
                    "Thank you! Your details have been entered. "
                    "The callback request is not yet saved or sent "
                    "to the company."
                )
