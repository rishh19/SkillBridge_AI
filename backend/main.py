from fastapi import FastAPI, UploadFile, File, Form
from services.resume_parser import extract_text_from_pdf
from services.ats_analyzer import analyze_candidate_for_job
import tempfile
import shutil
import os

app = FastAPI(
    title="SkillBridge AI Pro API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SkillBridge AI Pro API"
    }


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

        shutil.copyfileobj(resume.file, temp_file)

        temp_path = temp_file.name

    try:

        resume_text = extract_text_from_pdf(temp_path)

        result = analyze_candidate_for_job(
            resume_text,
            job_description
        )

        return result

    finally:

        os.remove(temp_path)