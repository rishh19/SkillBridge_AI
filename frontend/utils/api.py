import requests
import streamlit as st


BASE_URL = "https://skillbridge-ai-backend-mn6t.onrender.com"


def analyze_resume(resume, job_description):

    files = {
        "resume": (
            resume.name,
            resume.getvalue(),
            "application/pdf"
        )
    }

    data = {
        "job_description": job_description
    }

    try:

        response = requests.post(
            f"{BASE_URL}/analyze",
            files=files,
            data=data,
            timeout=120
        )

        if response.status_code == 200:

            return response.json()

        else:

            st.error(f"Status Code: {response.status_code}")
            st.code(response.text)

            return None

    except requests.exceptions.ConnectionError:

        st.error(
            """
Unable to connect to the backend.

Please make sure FastAPI is running.

Command:

uvicorn backend.main:app --reload
"""
        )

        return None

    except requests.exceptions.Timeout:

        st.error(
            "Request timed out. Please try again."
        )

        return None

    except Exception as e:

        st.error(str(e))

        return None