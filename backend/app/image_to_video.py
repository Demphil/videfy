from app.deepai_client import call_deepai

def generate_video_from_image(image_file):
    return call_deepai("https://api.deepai.org/api/torch-srgan", files={"image": image_file})
