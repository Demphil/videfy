import os
import requests
from gtts import gTTS
import cloudinary
import cloudinary.uploader

# إعداد Cloudinary
cloudinary.config(
    cloud_name="drfivaaqk",
    api_key="983925166616617",
    api_secret="Bfmj-xzKmruB8NDT5cfIhRaHZg8"
)

# إعداد مفتاح D-ID
DID_API_KEY = "Ym90b2xhcHJvc0BnbWFpbC5jb20:UDzhD73UeqWSOcY_hBfiA"

# 1. تحويل النص إلى صوت
def text_to_speech(text, output_file="output.mp3", lang="ar"):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    return output_file

# 2. رفع صورة إلى Cloudinary
def upload_image(image_path):
    result = cloudinary.uploader.upload(image_path)
    return result["secure_url"]

# 3. رفع صوت إلى D-ID
def upload_audio(audio_path):
    with open(audio_path, "rb") as f:
        response = requests.post(
            "https://api.d-id.com/audio",
            headers={"Authorization": f"api-key {DID_API_KEY}"},
            files={"audio": f}
        )
    if response.ok:
        return response.json()["url"]
    else:
        raise Exception(f"رفع الصوت فشل: {response.text}")

# 4. تحريك الصورة بالصوت
def animate_image(image_url, audio_url):
    payload = {
        "source_url": image_url,
        "audio_url": audio_url
    }

    response = requests.post(
        "https://api.d-id.com/talks",
        headers={
            "Authorization": f"api-key {DID_API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    if response.ok:
        talk_id = response.json()["id"]
        return talk_id
    else:
        raise Exception(f"فشل في إرسال الطلب: {response.text}")

# 5. جلب الفيديو النهائي
def get_video_url(talk_id):
    url = f"https://api.d-id.com/talks/{talk_id}"
    while True:
        res = requests.get(url, headers={"Authorization": f"api-key {DID_API_KEY}"})
        data = res.json()
        if data.get("result_url"):
            return data["result_url"]

# 🔁 تشغيل العملية الكاملة
def animate(text, image_path):
    print("🔊 تحويل النص إلى صوت...")
    audio_path = text_to_speech(text)

    print("📤 رفع الصورة إلى Cloudinary...")
    image_url = upload_image(image_path)

    print("🎧 رفع الصوت إلى D-ID...")
    audio_url = upload_audio(audio_path)

    print("🎞️ تحريك الصورة بالصوت...")
    talk_id = animate_image(image_url, audio_url)

    print("⏳ انتظار الفيديو...")
    video_url = get_video_url(talk_id)

    print("✅ الفيديو النهائي:", video_url)
    return video_url
