def preflight_render():
    try:
        write = nuke.thisNode()
        ruta = write['file'].value()
        if not ruta:
            raise RuntimeError(f"{write.name()}: sin ruta de salida definida")
        if not ruta.startswith('/mnt/productions/'):
            raise RuntimeError(f"{write.name()}: ruta fuera del servidor de produccion")
    except RuntimeError as e:
        nuke.message(str(e))
        raise  # cancela el render

nuke.addBeforeRender(preflight_render)
