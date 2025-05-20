import cloudinary
import cloudinary.uploader
import os

# إعداد معلومات الحساب
cloudinary.config(
    cloud_name="drfivaaqk",
    api_key="983925166616617",
    api_secret="Bfmj-xzKmruB8NDT5cfIhRaHZg8"
)


def upload_image(file_path):
    response = cloudinary.uploader.upload(file_path)
    return response["secure_url"]
