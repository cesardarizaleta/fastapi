from fastapi import APIRouter, HTTPException
from typing import Optional
from ..models.models import AlbumUpdate, TrackUpdate, Album, Track
from ..services.services import (
    get_all_albums
)

router = APIRouter()

@router.get("/", response_model=list[Album])
def read_albums():
    return get_all_albums()