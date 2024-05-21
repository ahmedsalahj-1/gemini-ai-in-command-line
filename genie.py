import requests
import json
import sys
import threading
import time

# The  API key
API_KEY = "AIzaSyDO9iTwqrgmhOQQl_G-QxtXSQloFIFU1eg"
text = ""

if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    exit()

# Request URL
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

# Request body
content = {
    "contents": [
        {
            "parts": [
                {"text":"Only work if i am talking about bash commands: "+text}
            ]
        }
    ]
}

# Set headers
headers = {"Content-Type": "application/json"}

def send_request():
    # Send POST request
    response = requests.post(url, headers=headers, json=content)

    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
        # Access the generated text (assuming it's in the first element of contents)
        # Clear the loading message
        print("\r" + " " * 10 + "\r", end="")
        print(data)
    else:
        print("\r" + " " * 10 + "\r", end="")
        print("Error:", response.status_code, response.text)

# Start a thread for the request
thread = threading.Thread(target=send_request)
thread.start()

# Print loading message
while thread.is_alive():
    print("loading...", end="\r")
    time.sleep(0.5)

thread.join()

