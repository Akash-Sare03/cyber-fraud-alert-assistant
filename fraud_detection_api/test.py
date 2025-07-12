import requests

# Your local Flask server
url = "http://127.0.0.1:5000/predict"

# Test message (change to anything scammy or normal)
data = {
    "message": "आपका बैंक खाता ब्लॉक कर दिया गया है। कृपया तुरंत संपर्क करें।"
}

# Send POST request
response = requests.post(url, json=data)

# Print API response
if response.status_code == 200:
    print("✅ API Response:")
    print(response.json())
else:
    print("❌ Error:", response.status_code)
    print(response.text)
