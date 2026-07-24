class StatusSummaryBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._labels: dict[str, QLabel] = {}
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        for status in ShotStatus:
            label = QLabel(f"{status.value}: 0")
            color = STATUS_COLORS[status.value].name()
            label.setStyleSheet(
                f"background-color: {color}; padding: 4px 8px;"
                f"border-radius: 4px; color: white;"
            )
            self._labels[status.value] = label
            layout.addWidget(label)
        layout.addStretch()

    def update_counts(self, shots: list[Shot]) -> None:
        counts: dict[str, int] = {s.value: 0 for s in ShotStatus}
        for shot in shots:
            counts[shot.status.value] += 1
        for status_val, label in self._labels.items():
            label.setText(f"{status_val}: {counts[status_val]}")
