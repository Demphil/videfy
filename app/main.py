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

# ملفات ثابتة (صور، جافاسكريبت، CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# رفع صورة (مثلاً للاستخدام العام)
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # هنا يمكن تخزين الملف مؤقتا إذا احتجت
    # مثلاً:
    # with open(f"temp/{file.filename}", "wb") as f:
    #     f.write(contents)
    return {"filename": file.filename, "size": len(contents)}

# توليد نص من مدخل نصي
@app.post("/generate-text")
async def api_generate_text(prompt: str = Form(...)):
    text = generate_text(prompt)
    return {"generated_text": text}

# تحويل صورة إلى فيديو
@app.post("/image-to-video")
async def api_image_to_video(image: UploadFile = File(...)):
    # استدعاء الدالة من app.image_to_video
    # تأكد أن generate_video_from_image تدعم UploadFile أو تحتاج تحويل
    video_path = await generate_video_from_image(image)
    return {"video_path": video_path}

# توليد وجه بناءً على وصف نصي
@app.post("/generate-face")
async def api_generate_face(description: str = Form(...)):
    face_url = generate_face(description)
    return {"face_url": face_url}

# تحليل صورة مع التعليق
@app.post("/analyze-image")
async def api_analyze_image(image: UploadFile = File(...)):
    analysis = await analyze_image(image)
    return {"analysis": analysis}

# تطبيق ستايل على صورة باستخدام صورة أخرى
@app.post("/style-transfer")
async def api_style_transfer(
    content_image: UploadFile = File(...),
    style_image: UploadFile = File(...)
):
    styled_image_path = await apply_style(content_image, style_image)
    return {"styled_image_path": styled_image_path}
