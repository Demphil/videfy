import requests

API_KEY = "your_deepai_api_key_here"

def call_deepai(api_url, files=None, data=None):
    headers = {"api-key": API_KEY}
    response = requests.post(api_url, files=files, data=data, headers=headers)
    return response.json()
