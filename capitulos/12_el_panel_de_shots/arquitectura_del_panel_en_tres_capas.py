from enum import Enum
from typing import Optional
from datetime import datetime, timezone
from pydantic import BaseModel

class ShotStatus(str, Enum):
    CREATED      = "created"
    INGESTED     = "ingested"
    IN_PROGRESS  = "in_progress"
    READY_FOR_QC = "ready_for_qc"
    QC_PENDING   = "qc_pending"
    QC_REJECTED  = "qc_rejected"
    APPROVED     = "approved"
    DELIVERED    = "delivered"
    ARCHIVED     = "archived"

VALID_TRANSITIONS: dict[ShotStatus, list[ShotStatus]] = {
    ShotStatus.CREATED:      [ShotStatus.INGESTED],
    ShotStatus.INGESTED:     [ShotStatus.IN_PROGRESS],
    ShotStatus.IN_PROGRESS:  [ShotStatus.READY_FOR_QC],
    ShotStatus.READY_FOR_QC: [ShotStatus.QC_PENDING, ShotStatus.IN_PROGRESS],
    ShotStatus.QC_PENDING:   [ShotStatus.QC_REJECTED, ShotStatus.APPROVED],
    ShotStatus.QC_REJECTED:  [ShotStatus.IN_PROGRESS],
    ShotStatus.APPROVED:     [ShotStatus.DELIVERED],
    ShotStatus.DELIVERED:    [ShotStatus.ARCHIVED],
    ShotStatus.ARCHIVED:     [],
}

class Shot(BaseModel):
    id: str
    name: str
    sequence: str
    status: ShotStatus = ShotStatus.CREATED
    frame_start: int
    frame_end: int
    compositor: Optional[str] = None
    notes: Optional[str] = None
    footage_path: Optional[str] = None
    script_path: Optional[str] = None
    status_changed_at: Optional[str] = None

    def transition_to(self, new_status: ShotStatus) -> None:
        allowed = VALID_TRANSITIONS.get(self.status, [])
        if new_status not in allowed:
            raise ValueError(
                f"Transición inválida: {self.status} → {new_status}"
            )
        self.status = new_status
        self.status_changed_at = datetime.now(timezone.utc).isoformat()
