from typing import List, Optional
from ..models.models import Album, Track, AlbumUpdate, TrackUpdate
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