import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "message": "आपका PAN कार्ड संदिग्ध गतिविधियों में उपयोग किया गया है।"
}

response = requests.post(url, json=data)
print(response.json())
