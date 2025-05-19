from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.middleware.cors import CORSMiddleware  # ✅ أضف هذا

from app.image_to_video import generate_video_from_image
from app.text_generator import generate_text
from app.image_captioning import analyze_image
from app.face_generator import generate_face
from app.style_transfer import apply_style

app = FastAPI()

# ✅ إعدادات CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://videfy.vercel.app"],  # يمكنك وضع ["*"] مؤقتًا أثناء التطوير
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Add endpoints for each feature here
