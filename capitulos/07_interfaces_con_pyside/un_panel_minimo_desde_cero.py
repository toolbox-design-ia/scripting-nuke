try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

class PanelEjemplo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Herramienta de ejemplo")
        self._build_ui()

    def _build_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("Nodos seleccionados: 0")
        layout.addWidget(self.label)

        self.btn_contar = QtWidgets.QPushButton("Contar nodos")
        self.btn_contar.clicked.connect(self._contar_nodos)
        layout.addWidget(self.btn_contar)

    def _contar_nodos(self):
        import nuke
        n = len(nuke.selectedNodes())
        self.label.setText(f"Nodos seleccionados: {n}")
