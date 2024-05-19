import requests
import json
import sys

# Replace with your actual API key
API_KEY = "AIzaSyDO9iTwqrgmhOQQl_G-QxtXSQloFIFU1eg"
text=""
if len(sys.argv)>1:
    text=sys.argv[1]
else:
    exit()
# Request URL
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

# Request body
content = {
    "contents": [
        {
            "parts": [
                {"text":"Only work if i am taiking about bash commands:  "+text}
            ]
        }
    ]
}

# Set headers
headers = {"Content-Type": "application/json"}

# Send POST request
response = requests.post(url, headers=headers, json=content)

# Check for successful response
if response.status_code == 200:
  # Parse the JSON response
  data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
  # Access the generated text (assuming it's in the first element of contents)
  print(data)
else:
  print("Error:",response.status_code,response.text)
