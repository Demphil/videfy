import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def upload_media_to_cloudinary(file_bytes, resource_type="auto"):
    try:
        result = cloudinary.uploader.upload(file_bytes, resource_type=resource_type)
        return result.get("secure_url")
    except Exception as e:
        raise RuntimeError(f"Upload failed: {str(e)}")
