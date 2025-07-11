import requests

url = "https://fraud-api-0lkm.onrender.com/predict"
data = {
    "message": "आपका PAN कार्ड ब्लॉक कर दिया गया है।"
}

response = requests.post(url, json=data)
print(response.json())
