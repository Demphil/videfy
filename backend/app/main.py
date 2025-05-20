from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()


from app.tts import text_to_speech
from app.cloudinary_uploader import upload_image
from app.animator import upload_audio, create_animation, get_result_url

app = FastAPI()

@app.post("/animate")
async def animate_image(text: str = Form(...), image: UploadFile = Form(...)):
    image_path = f"temp_{image.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # تحويل النص إلى صوت
    audio_path = text_to_speech(text)

    # رفع الصورة
    image_url = upload_image(image_path)

    # رفع الصوت
    audio_url = upload_audio(audio_path)

    # تحريك
    talk_id = create_animation(image_url, audio_url)
    result_url = get_result_url(talk_id)

    # حذف الملفات المؤقتة
    os.remove(image_path)
    os.remove(audio_path)

    return JSONResponse({"video_url": result_url})
