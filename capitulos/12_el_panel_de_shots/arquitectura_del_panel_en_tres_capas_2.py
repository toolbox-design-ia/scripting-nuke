import json
import os
from filelock import FileLock

class ShotRepository:
    def __init__(self, project_path: str):
        self.project_path = project_path
        self._shots_file = os.path.join(project_path, "shots.json")
        self._lock_file  = self._shots_file + ".lock"
        self._cache: dict[str, Shot] = {}

    def load_all(self) -> list[Shot]:
        with FileLock(self._lock_file):
            with open(self._shots_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        shots = [Shot(**s) for s in data]
        self._cache = {s.id: s for s in shots}
        return shots

    def save(self, shot: Shot) -> None:
        shots = self.load_all()
        updated = [shot if s.id == shot.id else s for s in shots]
        with FileLock(self._lock_file):
            with open(self._shots_file, "w", encoding="utf-8") as f:
                json.dump(
                    [s.model_dump(mode="json") for s in updated],
                    f,
                    indent=2
                )
        self._cache[shot.id] = shot
