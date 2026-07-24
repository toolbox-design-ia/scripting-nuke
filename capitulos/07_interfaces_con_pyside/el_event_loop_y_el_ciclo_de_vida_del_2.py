"""Extracto del patron defensivo impreso en el capitulo 7.

Estas lineas pertenecen a la clase del panel construida en este mismo
capitulo (archivo companero de esta carpeta): guardar el NOMBRE del
nodo, no el objeto, y resolverlo con nuke.toNode() antes de operar.
"""

# Al seleccionar un nodo en la interfaz
self.nodo_activo = nodo.name()

# Antes de cualquier operación posterior
def _operar_sobre_nodo(self):
    import nuke
    nodo = nuke.toNode(self.nodo_activo)
    if nodo is None:
        self.label_estado.setText("El nodo ya no existe en el script")
        return
    # ... continúa la operación
