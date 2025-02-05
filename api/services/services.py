from typing import List, Optional
from ..models.models import Album, Track, AlbumUpdate, TrackUpdate
import json

def get_all_albums() -> List[Album]:
    with open("api/data/data.json") as f:
        base = json.load(f)
    return base