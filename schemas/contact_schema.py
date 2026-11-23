from pydantic import BaseModel
from typing import Optional


class ContactSchema(BaseModel):

    name: str
    designation: Optional[str] = None
    department: Optional[str] = None
    contact_category: Optional[str] = None
    contact_priority: Optional[str] = None
    employment_status: Optional[str] = "unclear"
    linkedin_profile_url: Optional[str] = None
    public_email: Optional[str] = None
    source_url: Optional[str] = None
    evidence: Optional[str] = None
    hiring_relevance: Optional[str] = None