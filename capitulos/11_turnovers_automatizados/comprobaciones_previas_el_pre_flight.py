import hiero.core
import os

def check_media_accessible(sequence):
    errors = []
    for track in sequence.videoTracks():
        for item in track.items():
            clip = item.source()
            media_source = clip.mediaSource()
            path = media_source.fileinfos()[0].filename()
            if not os.path.isfile(path):
                errors.append(f"Media offline: {clip.name()} -> {path}")
    return errors
