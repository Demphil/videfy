from app.deepai_client import call_deepai

def generate_face():
    return call_deepai("https://api.deepai.org/api/fake-image")
