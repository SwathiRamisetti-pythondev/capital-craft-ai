
import streamlit as st
import csv
import os
from datetime import datetime


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
                file_path = "callback_requests.csv"
                file_exists = (
                    os.path.exists(file_path)
                    and os.path.getsize(file_path) > 0
                )

                with open(
                    file_path,
                    "a",
                    newline="",
                    encoding="utf-8",
                ) as file:
                    writer = csv.writer(file)

                    if not file_exists:
                        writer.writerow([
                            "Date and Time",
                            "Full Name",
                            "Email Address",
                            "Phone Number",
                            "Service",
                        ])

                    writer.writerow([
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                        name.strip(),
                        email.strip(),
                        phone.strip(),
                        service,
                    ])

                st.success(
                    "Thank you! Your callback request "
                    "has been saved successfully."
                )
