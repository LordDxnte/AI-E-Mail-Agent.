import os

from dotenv import load_dotenv

from groq import Groq

import imaplib

import email

from email.header import decode_header

import requests

from litellm import completion


# 1. CREDENTIALS

api_key = os.environ.get("GROQ_API_KEY")

webhook_url = os.environ.get("DISCORD_WEBHOOK")

email_user = os.environ.get("EMAIL_ACCOUNT")

email_pass = os.environ.get("EMAIL_PASSWORD")

# 2. THE EYES (Gmail)

print("Connecting to Gmail...")

mail = imaplib.IMAP4_SSL('imap.gmail.com')

mail.login(email_user, email_pass)

mail.select('inbox')

_, messages = mail.search(None, 'UNSEEN')

email_ids = messages[0].split()


unread_data = []

for e_id in email_ids[-10:]:

    res, msg_data = mail.fetch(e_id, '(RFC822)')

    for response_part in msg_data:

        if isinstance(response_part, tuple):

            msg = email.message_from_bytes(response_part[1])

            subject, encoding = decode_header(msg["Subject"])[0]

            if isinstance(subject, bytes):

                subject = subject.decode(encoding if encoding else "utf-8")

            unread_data.append(f"From: {msg.get('From')}\nSubject: {subject}")


raw_text = "\n---\n".join(unread_data) if unread_data else "No new emails."


# 3. THE BRAIN (Groq)

print("Asking AI to summarize...")

response = completion(

    model="groq/llama-3.1-8b-instant",

    messages=[{"role": "user", "content": f"Summarize and categorize these emails briefly:\n{raw_text}"}],

    client = Groq(api_key=api_key)

)

summary = response.choices[0].message.content


# 4. THE MOUTH (Discord)

requests.post(webhook_url, json={"content":f"**DAILY BRIEF**\n{summary}"})
response = requests.post(webhook_url, json={"content": "AI Agent is online!"})

print(f"Discord Response Code: {response.status_code}")
print(f"Discord Response Text: {response.text}")

print("✅ Done! Check Discord.")

