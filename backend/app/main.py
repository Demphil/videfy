from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
import shutil, os, uuid

from app.image_to_video import images_to_video
from app.text_to_audio import text_to_audio
from app.merge_audio_video import merge_audio_video
from app.deepai_client import generate_image_from_text

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ---------- صفحة رئيسية ----------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ---------- endpoint: صور > فيديو + سكريبت ----------
@app.post("/create-video", response_class=HTMLResponse)
async def create_video(
    request: Request,
    files: List[UploadFile] = File(...),
    script: str = Form(...),
    lang: str = Form("ar"),
    quality: str = Form("720")
):
    # 1) حفظ الصور
    image_paths = []
    for file in files:
        path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4().hex}_{file.filename}")
        with open(path, "wb") as buf:
            shutil.copyfileobj(file.file, buf)
        image_paths.append(path)

    # 2) إنشاء فيديو من الصور
    height = 1080 if quality == "1080" else 720
    video_path = images_to_video(image_paths, height=height)

    # 3) تحويل النص إلى صوت
    audio_path = text_to_audio(script, lang=lang)

    # 4) دمج الصوت مع الفيديو
    final_path = merge_audio_video(video_path, audio_path)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "video_url": f"/{final_path}",
        "message": "✅ تمت العملية بنجاح!"
    })

# ---------- endpoint: DeepAI Image ----------
@app.post("/generate-image", response_class=HTMLResponse)
async def generate_image(request: Request, prompt: str = Form(...)):
    img_url = generate_image_from_text(prompt)
    return templates.TemplateResponse("result.html", {
        "request": request,
        "image_url": img_url
    })
