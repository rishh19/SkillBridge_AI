# 🚀 SkillBridge AI Pro

<div align="center">

### AI-Powered Resume Intelligence Platform

Analyze resumes, evaluate ATS compatibility, identify skill gaps, match resumes with job descriptions, and receive personalized career recommendations.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.138-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.58-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=black)](https://render.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/rishh19/SkillBridge_AI)

</div>

---

# 📌 Overview

SkillBridge AI Pro is an AI-powered career intelligence platform that helps job seekers evaluate their resumes against real job descriptions.

The platform extracts information from resumes, compares it with job requirements, calculates an ATS compatibility score, identifies missing skills, and generates personalized recommendations to improve interview readiness.

The application is built using a modular FastAPI backend and an interactive Streamlit frontend, making it suitable for real-world deployment and scalable future development.

---

# 🌐 Live Demo

## Frontend

https://skillbridge-ai-frontend-2loi.onrender.com

## Backend API

https://skillbridge-ai-backend-mn6t.onrender.com

---

# ✨ Features

- ATS Resume Analysis
- Resume Parsing from PDF
- Job Description Analysis
- Resume vs Job Matching
- ATS Compatibility Score
- Missing Skills Detection
- Candidate Profile Generation
- Personalized Career Recommendations
- Interactive Dashboard
- Resume Upload Interface
- Dark / Light Theme
- Cloud Deployment using Render

---

# 🏗 System Architecture

```
Resume PDF
      │
      ▼
Resume Parser
      │
      ▼
Candidate Profile Builder
      │
      ▼
Job Description Parser
      │
      ▼
Matching Engine
      │
      ▼
ATS Score Engine
      │
      ▼
Recommendation Engine
      │
      ▼
Interactive Dashboard
```

---

# 📂 Project Structure

```
SkillBridge_AI/

│
├── backend/
│   ├── services/
│   ├── models/
│   ├── data/
│   └── main.py
│
├── frontend/
│   ├── assets/
│   ├── components/
│   ├── utils/
│   └── app.py
│
├── docs/
│
├── test_files/
│
├── test_resumes/
│
├── requirements.txt
│
└── README.md
```

---

# 🛠 Tech Stack

## Frontend

- Streamlit

## Backend

- FastAPI

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- PyMuPDF
- Requests

## Deployment

- Render

## Version Control

- Git
- GitHub

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/rishh19/SkillBridge_AI.git

cd SkillBridge_AI
```

---

## Create Virtual Environment

```bash
python -m venv skillbridge_venv
```

Activate

Windows

```bash
skillbridge_venv\Scripts\activate
```

Linux / macOS

```bash
source skillbridge_venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run Backend

```bash
cd backend

uvicorn main:app --reload
```

Backend will run on

```
http://127.0.0.1:8000
```

---

# ▶ Run Frontend

```bash
cd frontend

streamlit run app.py
```

Frontend will run on

```
http://localhost:8501
```

---

# 📊 API Endpoint

## Home

```
GET /
```

Returns

```json
{
    "message":"Welcome to SkillBridge AI Pro API"
}
```

---

## Analyze Resume

```
POST /analyze
```

Input

- Resume PDF
- Job Description

Output

- ATS Score
- Skill Match
- Missing Skills
- Candidate Analysis
- Personalized Recommendations

---

# 📸 Screenshots

Create a folder named

```
screenshots/
```

and add

- Home Page
- Resume Upload
- ATS Analysis
- Dashboard
- Recommendations

Then update this section.

---

# 🎯 Future Enhancements

- Authentication
- Resume History
- Multiple Resume Comparison
- AI Chatbot
- LLM Integration
- PDF Report Export
- Docker Support
- PostgreSQL Database
- AWS Deployment
- CI/CD Pipeline

---

# 🎓 Learning Outcomes

This project helped strengthen practical skills in:

- FastAPI Development
- Streamlit Development
- REST APIs
- Resume Parsing
- ATS Analysis
- Machine Learning Workflows
- Software Architecture
- Git & GitHub
- Cloud Deployment
- Modular Python Development

---

# 👨‍💻 Author

**Rishav Kumar Shrivastava**

B.Tech Computer Science Engineering

KIIT University

GitHub

https://github.com/rishh19

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### Thank you for visiting SkillBridge AI Pro ❤️

Made with Python, FastAPI, Streamlit and lots of ☕.

</div>
