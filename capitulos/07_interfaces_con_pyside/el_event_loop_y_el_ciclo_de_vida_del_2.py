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
