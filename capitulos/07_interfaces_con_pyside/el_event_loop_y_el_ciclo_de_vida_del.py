import sys

try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

def obtener_app():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    return app
