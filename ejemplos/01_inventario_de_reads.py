"""Inventario de los Read del script, con aviso de archivos que faltan.

Solo lectura. Util antes de entregar o al abrir un script heredado: dice de
un vistazo que material referencia y que referencias estan rotas.
"""
import os

import nuke


def frame_exists(read_node, frame):
    """Comprueba la existencia del archivo de un frame concreto."""
    ruta = nuke.filename(read_node, nuke.REPLACE)
    if not ruta:
        return False
    try:
        return os.path.exists(ruta % frame)
    except TypeError:  # ruta sin patron de numeracion
        return os.path.exists(ruta)


def main():
    reads = nuke.allNodes("Read")
    if not reads:
        print("El script no tiene nodos Read.")
        return

    print(f"{len(reads)} nodos Read\n")
    rotos = []
    for node in reads:
        primero = int(node["first"].value())
        ultimo = int(node["last"].value())
        completo = frame_exists(node, primero) and frame_exists(node, ultimo)
        estado = "ok" if completo else "FALTA"
        if not completo:
            rotos.append(node.name())
        print(f"  [{estado:5}] {node.name()[:22]:22} "
              f"{primero}-{ultimo}  {node['file'].value()[:60]}")

    if rotos:
        print(f"\nAtencion: {len(rotos)} lecturas apuntan a archivos que no "
              f"se encuentran: {', '.join(rotos)}")
    else:
        print("\nTodas las lecturas resuelven a archivos existentes.")


if __name__ == "__main__":
    main()
