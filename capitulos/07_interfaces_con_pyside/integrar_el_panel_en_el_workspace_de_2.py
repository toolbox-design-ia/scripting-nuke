class DialogoConfirmacion(QtWidgets.QDialog):
    def __init__(self, mensaje, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmar")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel(mensaje))

        botones = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        )
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)

def pedir_confirmacion(mensaje):
    dialogo = DialogoConfirmacion(mensaje)
    return dialogo.exec_() == QtWidgets.QDialog.Accepted
