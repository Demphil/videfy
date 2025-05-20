from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.animator import animate_image
from app.cloudinary_uploader import upload_media_to_cloudinary

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload-animate", response_class=HTMLResponse)
async def upload_and_animate(request: Request, file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()

        # ✅ 1. تحريك الصورة
        animated_bytes = animate_image(file_bytes)

        # ✅ 2. رفع النتيجة إلى Cloudinary
        animated_url = upload_media_to_cloudinary(animated_bytes, resource_type="video")

        return templates.TemplateResponse("index.html", {
            "request": request,
            "video_url": animated_url
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e)
        })
