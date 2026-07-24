def auditar_composicion():
    errores = []
    for node in nuke.allNodes('Read'):
        ruta = node['file'].value()
        if not ruta:
            errores.append(f"READ SIN RUTA: {node.name()}")
        elif not ruta.startswith('/mnt/productions/'):
            errores.append(f"RUTA NO AUTORIZADA: {node.name()} -> {ruta}")
    for node in nuke.allNodes('Write'):
        if not node['file'].value():
            errores.append(f"WRITE SIN SALIDA: {node.name()}")
    return errores
