def _filtrar_reads(self):
    import nuke
    patron = self.campo_path.text().strip()
    if not patron:
        return

    # Deseleccionar todo primero
    for nodo in nuke.allNodes():
        nodo.setSelected(False)

    encontrados = 0
    for nodo in nuke.allNodes("Read"):
        path = nodo["file"].value()
        if patron in path:
            nodo.setSelected(True)
            encontrados += 1

    self.label_resultado.setText(f"{encontrados} Read(s) encontrados")
