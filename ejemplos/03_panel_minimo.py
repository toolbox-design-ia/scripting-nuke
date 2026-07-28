"""Panel PySide minimo y acoplable: el esqueleto de cualquier herramienta.

Registra un panel con un boton que actua sobre la seleccion. Copialo como
punto de partida y sustituye run_action() por lo que necesites.

Uso: ejecutar en el Script Editor, o llamar register_panel() desde menu.py.
"""
try:
    from PySide6 import QtWidgets
except ImportError:  # Nuke 14 y 15 traen PySide2
    from PySide2 import QtWidgets

import nuke
import nukescripts


class StudioPanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel("Selecciona nodos y pulsa el boton.")
        boton = QtWidgets.QPushButton("Informar de la seleccion")
        boton.clicked.connect(self.run_action)
        layout.addWidget(self.label)
        layout.addWidget(boton)
        layout.addStretch()

    def run_action(self):
        seleccion = nuke.selectedNodes()
        if not seleccion:
            self.label.setText("No hay nada seleccionado.")
            return
        tipos = {}
        for node in seleccion:
            tipos[node.Class()] = tipos.get(node.Class(), 0) + 1
        resumen = ", ".join(f"{n} x{c}" for n, c in sorted(tipos.items()))
        self.label.setText(f"{len(seleccion)} nodos: {resumen}")


def register_panel():
    """Registra el panel para poder acoplarlo como cualquier otro."""
    nukescripts.registerWidgetAsPanel(
        f"{__name__}.StudioPanel", "Panel de estudio",
        "studio35.panels.StudioPanel", True)


if __name__ == "__main__":
    register_panel()
