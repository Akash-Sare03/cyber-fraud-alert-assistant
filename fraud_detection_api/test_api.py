import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "message": "आपका PAN कार्ड संदिग्ध गतिविधियों में उपयोग किया गया है।"
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.text)  # Print full HTML or message
