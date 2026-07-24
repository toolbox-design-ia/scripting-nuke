"""
publish_tool.py — Despliega una herramienta al entorno de producción
con checksums y metadatos de trazabilidad.
Uso: python publish_tool.py --config publish_config.json
"""

import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def build_version_dir(base: Path, config: dict) -> Path:
    version_dir = base / config["category"] / config["tool"] / config["version"]
    # exist_ok=False: falla si la versión ya existe en producción
    version_dir.mkdir(parents=True, exist_ok=False)
    return version_dir


def copy_artifacts(source_dir: Path, dest_dir: Path, platforms: list) -> list:
    copied = []
    for platform in platforms:
        src_platform = source_dir / platform
        dst_platform = dest_dir / platform
        if src_platform.exists():
            shutil.copytree(src_platform, dst_platform)
            for f in dst_platform.rglob("*"):
                if f.is_file():
                    copied.append(f)
    for pattern in ["*.nk", "*.py", "README.md", "CHANGELOG.md", "VERSION"]:
        for f in source_dir.glob(pattern):
            dest = dest_dir / f.name
            shutil.copy2(f, dest)
            copied.append(dest)
    return copied


def write_checksums(files: list, dest_dir: Path) -> None:
    entries = []
    for file_path in sorted(files):
        checksum = sha256_file(file_path)
        relative = file_path.relative_to(dest_dir)
        entries.append(f"{checksum}  {relative}")
    checksum_file = dest_dir / "CHECKSUMS.sha256"
    checksum_file.write_text("\n".join(entries) + "\n")


def write_delivery_metadata(dest_dir: Path, config: dict, published_by: str) -> Path:
    metadata = {
        "tool": config["tool"],
        "category": config["category"],
        "version": config["version"],
        "build_date": config["build_date"],
        "published_at": datetime.now(timezone.utc).isoformat(),
        "published_by": published_by,
        "git_branch": config.get("git_branch", ""),
        "git_commit": config.get("git_commit", ""),
        "platforms": config.get("platforms", []),
        "nuke_versions": config.get("nuke_versions", []),
        "checksum_file": "CHECKSUMS.sha256",
        "notes": config.get("notes", ""),
    }
    delivery_file = dest_dir / "DELIVERY.json"
    delivery_file.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n")
    return delivery_file


def publish(config_path: Path) -> None:
    config = json.loads(config_path.read_text())
    prod_base = Path(config["prod_base"])
    source_dir = Path(config["source_dir"])
    published_by = os.environ.get("USER", "unknown")

    print(f"Publicando {config['tool']} {config['version']}...")
    version_dir = build_version_dir(prod_base, config)
    files = copy_artifacts(source_dir, version_dir, config.get("platforms", []))
    delivery_file = write_delivery_metadata(version_dir, config, published_by)
    write_checksums(files + [delivery_file], version_dir)
    print(f"Publicado en: {version_dir}")
    print(f"Checksums:    {version_dir / 'CHECKSUMS.sha256'}")
    print(f"Metadatos:    {version_dir / 'DELIVERY.json'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, type=Path)
    args = parser.parse_args()
    publish(args.config)
