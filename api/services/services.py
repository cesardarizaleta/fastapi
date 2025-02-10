from typing import List, Optional
from ..models.models import Album, Track
import json

DATA_FILE = "api/data/data.json"

def load_data():
    if DATA_FILE.endswith(".json"):
        with open(DATA_FILE) as f:
            return json.load(f)


def get_all_albums() -> List[Album]:
    return load_data()

def get_album_by_id(album_id: int) -> Optional[Album]:
    data = load_data()
    return next((album for album in data if album["id"] == album_id), None)

def get_tracks_by_album_id(album_id: int) -> Optional[List[Track]]:
    album = get_album_by_id(album_id)
    return album.get("tracks") if album else None

def get_track_by_id(album_id: int, track_id: int) -> Optional[Track]:
    tracks = get_tracks_by_album_id(album_id)
    return next((track for track in tracks if track["number"] == track_id), None)