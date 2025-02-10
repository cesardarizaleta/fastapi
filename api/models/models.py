from pydantic import BaseModel
from typing import List

class Track(BaseModel):
    number: int
    title: str
    duration: str

class Album(BaseModel):
    id: int
    title: str
    year: int
    tracks: List[Track]