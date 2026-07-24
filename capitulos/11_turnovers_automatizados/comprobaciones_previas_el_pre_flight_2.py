def check_framerate_consistency(sequence):
    seq_fps = sequence.framerate()
    mismatches = []
    for track in sequence.videoTracks():
        for item in track.items():
            clip_fps = item.source().framerate()
            if abs(float(clip_fps) - float(seq_fps)) > 0.001:
                mismatches.append(
                    f"{item.source().name()}: {clip_fps} != {seq_fps}"
                )
    return mismatches
