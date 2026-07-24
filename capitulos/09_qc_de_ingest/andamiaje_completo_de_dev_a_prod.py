# tests/test_frame_range.py
from pathlib import Path
import pytest
from dev.qc_ingest import analyze_frame_range

def test_detects_missing_frame(tmp_path):
    # Crear secuencia con frame 1002 ausente.
    for i in [1001, 1003, 1004, 1005]:
        (tmp_path / f"test.{i:04d}.exr").touch()

    result = analyze_frame_range(str(tmp_path), "test.%04d.exr", 1001, 1005)

    assert result["complete"] is False
    assert 1002 in result["missing"]
    assert result["found_count"] == 4
    assert result["expected_count"] == 5

def test_passes_complete_sequence(tmp_path):
    for i in range(1001, 1006):
        (tmp_path / f"test.{i:04d}.exr").touch()

    result = analyze_frame_range(str(tmp_path), "test.%04d.exr", 1001, 1005)

    assert result["complete"] is True
    assert result["missing"] == []
