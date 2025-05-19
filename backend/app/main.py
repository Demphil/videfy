import shutil
import tempfile
from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.image_to_video import generate_video_from_image
from app.text_generator import generate_text
from app.image_captioning import analyze_image
from app.face_generator import generate_face
from app.style_transfer import apply_style

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

async def save_upload_file_tmp(upload_file: UploadFile) -> str:
    suffix = "." + upload_file.filename.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(upload_file.file, tmp)
        tmp_path = tmp.name
    return tmp_path

@app.get("/templates", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    tmp_path = await save_upload_file_tmp(file)
    # هنا يمكن التعامل مع الملف المؤقت (tmp_path)
    # مثلاً تخزينه أو تحليله
    # ثم حذف الملف المؤقت لو أردت بعد الانتهاء:
    # os.remove(tmp_path)
    return {"filename": file.filename, "temp_path": tmp_path}

@app.post("/generate-text")
async def api_generate_text(prompt: str = Form(...)):
    text = generate_text(prompt)
    return {"generated_text": text}

@app.post("/image-to-video")
async def api_image_to_video(image: UploadFile = File(...)):
    tmp_path = await save_upload_file_tmp(image)
    video_path = await generate_video_from_image(tmp_path)
    # بعد الانتهاء يمكنك حذف tmp_path إذا أردت
    return {"video_path": video_path}

@app.post("/generate-face")
async def api_generate_face(description: str = Form(...)):
    face_url = generate_face(description)
    return {"face_url": face_url}

@app.post("/analyze-image")
async def api_analyze_image(image: UploadFile = File(...)):
    tmp_path = await save_upload_file_tmp(image)
    analysis = await analyze_image(tmp_path)
    return {"analysis": analysis}

@app.post("/style-transfer")
async def api_style_transfer(
    content_image: UploadFile = File(...),
    style_image: UploadFile = File(...)
):
    tmp_content = await save_upload_file_tmp(content_image)
    tmp_style = await save_upload_file_tmp(style_image)
    styled_image_path = await apply_style(tmp_content, tmp_style)
    return {"styled_image_path": styled_image_path}
