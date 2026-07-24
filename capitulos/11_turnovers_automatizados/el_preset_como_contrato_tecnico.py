import shutil
import os

STUDIO_PRESETS_DIR = "/mnt/studio/tools/hiero_presets"
USER_PRESETS_DIR = os.path.expanduser("~/.hiero/presets")

def install_presets():
    os.makedirs(USER_PRESETS_DIR, exist_ok=True)
    for preset_file in os.listdir(STUDIO_PRESETS_DIR):
        src = os.path.join(STUDIO_PRESETS_DIR, preset_file)
        dst = os.path.join(USER_PRESETS_DIR, preset_file)
        shutil.copy2(src, dst)
