import requests


# Paste your new webhook URL here

webhook_url = "https://discord.com/api/webhooks/1498052495887569107/r4UgwISOKZCezbT-llFppD5g02n1ai6lhw2xQWE-2tluxgjuyjL6MXrV-Dr3gSDwn3Ne"


data = {

    "content": "🚀 **Diagnostic Test:** The error handler is working."

}


print("Initiating connection to Discord...")


try:

    # Attempting to send the message

    response = requests.post(webhook_url, json=data)

    

    # Checking Discord's response

    if response.status_code == 204:

        print("✅ SUCCESS: Message successfully sent to Discord!")

    else:

        print(f"❌ REJECTED: Discord blocked the message. Status Code: {response.status_code}")

        print(f"Discord says: {response.text}")


except requests.exceptions.MissingSchema:

    print("⚠️ FORMAT ERROR: Your webhook URL is missing the 'https://' part.")

except Exception as e:

    print(f"💥 CRASH: Python failed to execute. The exact error is: {e}")
