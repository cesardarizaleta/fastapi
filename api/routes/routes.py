from fastapi import APIRouter, HTTPException
from typing import Optional
from ..models.models import AlbumUpdate, TrackUpdate, Album, Track
from ..services.services import (
    get_all_albums,
    get_album_by_id
)

router = APIRouter()

@router.get("/", response_model=list[Album])
def read_albums():
    return get_all_albums()

@router.get("/{album_id}", response_model=Album)
def read_album(album_id: int):
    album = get_album_by_id(album_id)
    if album is None:
        raise HTTPException(status_code=404, detail="Album not found")
    return album