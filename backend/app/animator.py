import requests
import time

DID_API_KEY = "YOUR_DID_API_KEY"
DID_API_URL = "https://api.d-id.com"

HEADERS = {
    "Authorization": f"Bearer {DID_API_KEY}"
}

def upload_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        files = {'file': audio_file}
        response = requests.post(f"{DID_API_URL}/upload", headers=HEADERS, files=files)
    
    if response.status_code == 200:
        return response.json()["url"]
    else:
        raise Exception("❌ فشل في رفع الصوت إلى D-ID")

def create_talking_video(image_url, audio_url):
    payload = {
        "source_url": image_url,
        "script": {
            "type": "audio",
            "audio_url": audio_url
        }
    }

    response = requests.post(f"{DID_API_URL}/talks", json=payload, headers=HEADERS)

    if response.status_code == 201:
        return response.json()["id"]
    else:
        raise Exception("❌ فشل في إنشاء الفيديو على D-ID")

def get_video_url(talk_id):
    for _ in range(30):  # انتظار لحد 30 ثانية كحد أقصى
        time.sleep(2)
        response = requests.get(f"{DID_API_URL}/talks/{talk_id}", headers=HEADERS)

        if response.status_code == 200:
            data = response.json()
            if data["status"] == "done":
                return data["result_url"]
        else:
            raise Exception("❌ فشل في التحقق من حالة الفيديو")
    
    raise Exception("⏳ انتهى الوقت دون إنشاء الفيديو")

def animate_image_with_audio(image_url, audio_path):
    print("⏫ رفع الصوت...")
    audio_url = upload_audio(audio_path)

    print("🎬 بدء تحريك الصورة...")
    talk_id = create_talking_video(image_url, audio_url)

    print("⏳ انتظار اكتمال الفيديو...")
    video_url = get_video_url(talk_id)

    print("✅ الفيديو جاهز!")
    return video_url
