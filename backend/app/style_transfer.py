from app.deepai_client import call_deepai

def apply_style(content_image, style_image):
    return call_deepai("https://api.deepai.org/api/neural-style", files={
        "content": content_image,
        "style": style_image,
    })
