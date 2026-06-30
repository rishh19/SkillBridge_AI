from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class CandidateProfile(BaseModel):

    candidate_name: Optional[str] = None

    education: List[Dict[str, Any]] = Field(default_factory=list)

    skills: List[str] = Field(default_factory=list)

    projects: List[Dict[str, Any]] = Field(default_factory=list)

    certifications: List[Dict[str, Any]] = Field(default_factory=list)

    experience: List[Dict[str, Any]] = Field(default_factory=list)

    primary_domain: Optional[str] = None

    secondary_domain: Optional[str] = None

    strengths: List[str] = Field(default_factory=list)

    weaknesses: List[str] = Field(default_factory=list)

    raw_resume_text: str = ""