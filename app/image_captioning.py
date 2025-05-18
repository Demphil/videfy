from app.deepai_client import call_deepai

def analyze_image(image_file):
    return call_deepai("https://api.deepai.org/api/image-captioning", files={"image": image_file})
