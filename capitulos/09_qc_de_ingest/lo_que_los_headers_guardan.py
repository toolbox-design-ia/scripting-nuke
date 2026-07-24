import OpenEXR
import Imath

def read_exr_metadata(filepath: str) -> dict:
    exr = OpenEXR.InputFile(filepath)
    header = exr.header()

    dw = header["dataWindow"]
    width = dw.max.x - dw.min.x + 1
    height = dw.max.y - dw.min.y + 1

    channels = list(header["channels"].keys())

    colorspace = header.get("colorSpace", b"").decode("utf-8", errors="ignore")

    pixel_types = {
        ch: str(header["channels"][ch].type)
        for ch in channels
    }

    return {
        "width": width,
        "height": height,
        "channels": channels,
        "colorspace": colorspace or None,
        "pixel_types": pixel_types,
    }
