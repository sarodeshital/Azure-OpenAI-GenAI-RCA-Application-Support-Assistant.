from pydantic import BaseModel, Field
from typing import List


class IncidentRequest(BaseModel):
    incident_id: str = Field(min_length=1)
    service: str = Field(min_length=1)
    error_code: str = Field(min_length=1)
    description: str = Field(min_length=1)
    logs: List[str] = []
