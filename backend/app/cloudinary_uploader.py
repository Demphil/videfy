import cloudinary
import cloudinary.uploader

# إعداد معلومات الحساب
cloudinary.config(
    cloud_name="drfivaaqk",
    api_key="983925166616617",
    api_secret="Bfmj-xzKmruB8NDT5cfIhRaHZg8"
)

def upload_image_to_cloudinary(image_path):
    try:
        response = cloudinary.uploader.upload(image_path)
        return response["secure_url"]
    except Exception as e:
        print("❌ خطأ في رفع الصورة:", e)
        return None
