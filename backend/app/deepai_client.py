import requests

API_KEY = "a42fafad-3212-4e5c-8bad-e2646cefe8e1"

def call_deepai(api_url, files=None, data=None):
    headers = {"api-key": API_KEY}
    response = requests.post(api_url, files=files, data=data, headers=headers)
    return response.json()
