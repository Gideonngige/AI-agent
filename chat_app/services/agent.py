from google import genai

from dotenv import load_dotenv
load_dotenv()
import os
from chat_app.utils import generate_business_report, send_report_email
from datetime import datetime

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

def ask_agent(message):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message
    )

    return response.text


from .tools import (get_total_customers,get_total_sales)

def ask_agent2(message):
    message_lower = message.lower()

    # DEBUG (IMPORTANT)
    print("USER MESSAGE:", message_lower)

    if "customer" in message_lower or "customers" in message_lower:
        print("Getting total customers...")
        return f"You have {get_total_customers()} customers."

    if "sale" in message_lower or "sales" in message_lower:
        print("Getting total sales...")
        return f"Total sales are KES {get_total_sales()}"

    # ONLY if no match → Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
            You are a business assistant.

            Known data:
            - Customers: {get_total_customers()}
            - Sales: KES {get_total_sales()}

            User question: {message}

            Give a clear business answer.
        """
    )

    return response.text


def ask_agent3(message, email):
    message_lower = message.lower()

    if "report" in message_lower:
        customers = get_total_customers()
        sales = get_total_sales()
        # generate report from AI agent
        paragraph = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
                You are a business assistant.

                Known data:
                - Current date: {datetime.now()}
                - Department: Sales
                - Customers: {customers}
                - Sales: KES {sales}

                User request: {message}

                Generate a concise business report based on the above data and user request.
            """
        )

        file_path = generate_business_report(customers, sales, paragraph.text)

        send_report_email(file_path, email)

        return "Report generated and sent to your email."

    return "I don't understand the request."