from pydantic import BaseModel
from typing import Optional, List

class Track(BaseModel):
    number: int
    title: str
    duration: str

class Album(BaseModel):
    id: int
    title: str
    year: int
    tracks: List[Track]

class TrackUpdate(BaseModel):
    number: Optional[int] = None
    title: Optional[str] = None
    duration: Optional[str] = None

class AlbumUpdate(BaseModel):
    id: Optional[int]
    title: Optional[str] = None
    year: Optional[int] = None
    tracks: Optional[List[Track]] = None