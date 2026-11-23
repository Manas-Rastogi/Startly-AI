from pydantic import BaseModel
from typing import Optional


class StartupSchema(BaseModel):

    startup_name: str
    category: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    funding_amount: Optional[float] = None
    funding_stage: Optional[str] = None
    funding_date: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None
    source_url: Optional[str] = None