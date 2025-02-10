from fastapi import APIRouter, HTTPException
from typing import Optional
from ..models.models import Album, Track
from ..services.services import (
    get_all_albums,
    get_album_by_id,
    get_tracks_by_album_id,
    get_track_by_id
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

@router.get("/{album_id}/tracks", response_model= list[Track])
def read_tracks(album_id: int):
    tracks = get_tracks_by_album_id(album_id)
    if tracks is None:
        raise HTTPException(status_code=404, detail="Tracks not found")
    return tracks

@router.get("/{album_id}/{track_id}", response_model= Track)
def read_track(album_id: int, track_id: int):
    track = get_track_by_id(album_id, track_id)
    if track is None:
        raise HTTPException(status_code=404, detail="Track not found") 
    return track