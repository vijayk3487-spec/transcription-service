from pydantic import BaseModel
from typing import List

class Segment(BaseModel):
    start: float
    end: float
    text: str

class TranscriptionResponse(BaseModel):
    filename: str
    segments: List[Segment]