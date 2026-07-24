from PySide2.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QTableView, QPushButton, QLabel,
    QComboBox, QHeaderView
)
from PySide2.QtGui import QStandardItemModel, QStandardItem, QColor
from PySide2.QtCore import Qt

COLUMNS = ["ID", "Nombre", "Secuencia", "Estado", "Compositor", "Frames", "Notas"]

STATUS_COLORS = {
    "created":      QColor(100, 100, 100),
    "ingested":     QColor(70,  130, 180),
    "in_progress":  QColor(255, 165,   0),
    "ready_for_qc": QColor(220, 200,   0),
    "qc_pending":   QColor(180, 180,   0),
    "qc_rejected":  QColor(200,  50,  50),
    "approved":     QColor(50,  180,  50),
    "delivered":    QColor(50,  120,  50),
    "archived":     QColor(150, 150, 150),
}

class ShotPanel(QWidget):
    def __init__(self, repo: ShotRepository, parent=None):
        super().__init__(parent)
        self.repo = repo
        self._setup_ui()
        self.refresh()

    def _setup_ui(self):
        layout = QVBoxLayout(self)

        controls = QHBoxLayout()
        self.filter_combo = QComboBox()
        self.filter_combo.addItem("Todos los estados")
        for status in ShotStatus:
            self.filter_combo.addItem(status.value)
        self.filter_combo.currentIndexChanged.connect(self._apply_filter)

        refresh_btn = QPushButton("Refrescar")
        refresh_btn.clicked.connect(self.refresh)

        self.status_label = QLabel("")
        controls.addWidget(QLabel("Filtro:"))
        controls.addWidget(self.filter_combo)
        controls.addStretch()
        controls.addWidget(self.status_label)
        controls.addWidget(refresh_btn)
        layout.addLayout(controls)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(COLUMNS)

        self.table = QTableView()
        self.table.setModel(self.model)
        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setEditTriggers(QTableView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.Stretch
        )
        layout.addWidget(self.table)

    def refresh(self):
        shots = self.repo.load_all()
        self._populate(shots)
        self.status_label.setText(f"{len(shots)} planos cargados")

    def _populate(self, shots: list[Shot]):
        self.model.removeRows(0, self.model.rowCount())
        for shot in shots:
            frame_count = shot.frame_end - shot.frame_start + 1
            row = [
                QStandardItem(shot.id),
                QStandardItem(shot.name),
                QStandardItem(shot.sequence),
                QStandardItem(shot.status.value),
                QStandardItem(shot.compositor or "—"),
                QStandardItem(str(frame_count)),
                QStandardItem(shot.notes or ""),
            ]
            color = STATUS_COLORS.get(shot.status.value, QColor(255, 255, 255))
            for item in row:
                item.setBackground(color)
            self.model.appendRow(row)

    def _apply_filter(self):
        selected = self.filter_combo.currentText()
        for row in range(self.model.rowCount()):
            status_item = self.model.item(row, 3)
            if selected == "Todos los estados":
                self.table.setRowHidden(row, False)
            else:
                self.table.setRowHidden(row, status_item.text() != selected)
