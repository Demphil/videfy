import requests

def generate_image_from_text(prompt: str) -> str:
    response = requests.post(
        "https://api.deepai.org/api/text2img",
        data={"text": prompt},
        headers={"api-key": "a42fafad-3212-4e5c-8bad-e2646cefe8e1"}
    )
    result = response.json()
    return result.get("output_url", "")
