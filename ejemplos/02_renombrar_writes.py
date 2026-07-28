"""Aplica una convencion de nombres a los nodos Write.

Propone por defecto; solo escribe si se llama con aplicar=True. Ajusta
build_path() a la nomenclatura de tu estudio.
"""
import os

import nuke


def build_path(node, shot, version):
    """Ruta de salida segun convencion: /renders/<shot>/<shot>_<vNNN>.%04d.exr"""
    carpeta = os.path.join("/renders", shot)
    nombre = f"{shot}_v{version:03d}.%04d.exr"
    return os.path.join(carpeta, nombre)


def rename_writes(shot="SH0170", version=1, aplicar=False):
    writes = nuke.allNodes("Write")
    if not writes:
        print("El script no tiene nodos Write.")
        return

    print(f"{'APLICANDO' if aplicar else 'PROPUESTA (sin cambios)'} "
          f"- {len(writes)} nodos Write\n")
    for node in writes:
        actual = node["file"].value()
        nuevo = build_path(node, shot, version)
        if actual == nuevo:
            continue
        print(f"  {node.name()}")
        print(f"     antes: {actual}")
        print(f"     ahora: {nuevo}")
        if aplicar:
            node["file"].setValue(nuevo)
            node["file_type"].setValue("exr")

    if not aplicar:
        print("\nRevisa la propuesta y vuelve a llamar con aplicar=True.")


if __name__ == "__main__":
    rename_writes()
