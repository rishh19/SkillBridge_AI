from pydantic import BaseModel
from typing import List


class JobProfile(BaseModel):

    job_title: str = ""

    required_skills: List[str] = []

    preferred_skills: List[str] = []

    required_education: str = ""

    required_experience: str = ""

    responsibilities: List[str] = []

    raw_job_description: str = ""