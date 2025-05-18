from app.deepai_client import call_deepai

def generate_text(prompt):
    return call_deepai("https://api.deepai.org/api/text-generator", data={"text": prompt})
