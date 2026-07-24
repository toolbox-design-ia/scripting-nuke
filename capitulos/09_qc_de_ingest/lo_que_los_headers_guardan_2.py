import nuke

def read_metadata_via_nuke(file_pattern: str, frame: int) -> dict:
    n = nuke.nodes.Read(file=file_pattern, first=frame, last=frame)
    nuke.execute(n, frame, frame)

    result = {
        "width": n.width(),
        "height": n.height(),
        "channels": n.channels(),
        "colorspace": n["colorspace"].value(),
        "format": n.format().name(),
    }

    nuke.delete(n)
    return result
