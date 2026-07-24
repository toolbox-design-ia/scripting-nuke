import hashlib
from pathlib import Path

def sha256_file(path: Path) -> str:
    """Calcula el SHA-256 de un archivo en bloques para manejar archivos grandes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()

def write_checksums(directory: Path, output_file: Path) -> None:
    """Genera CHECKSUMS.sha256 con todos los archivos del directorio."""
    entries = []
    for file_path in sorted(directory.rglob("*")):
        if file_path.is_file() and file_path.name != "CHECKSUMS.sha256":
            checksum = sha256_file(file_path)
            relative = file_path.relative_to(directory)
            entries.append(f"{checksum}  {relative}")
    output_file.write_text("\n".join(entries) + "\n")
