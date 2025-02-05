from typing import List, Optional
from ..models.models import Album, Track, AlbumUpdate, TrackUpdate
from ..data.data import albums

def get_all_albums() -> List[Album]:
    return albums