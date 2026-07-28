"""Radiografia del entorno: version, rutas y donde busca Nuke los scripts.

Primer script que conviene ejecutar en una instalacion nueva: casi todos los
problemas de "mi herramienta no aparece" se explican con esta informacion.
"""
import os

import nuke


def main():
    print("Nuke", nuke.NUKE_VERSION_STRING)
    print("Ejecutable :", nuke.env["ExecutablePath"])
    print("Modo GUI   :", nuke.GUI)
    print("Threads    :", nuke.env["threads"])

    print("\nNUKE_PATH (donde busca init.py y menu.py):")
    rutas = os.environ.get("NUKE_PATH", "")
    if not rutas:
        print("  (sin definir: solo se usan las rutas por defecto)")
    for ruta in rutas.split(os.pathsep):
        if ruta:
            existe = "ok " if os.path.isdir(ruta) else "NO EXISTE"
            print(f"  [{existe}] {ruta}")

    print("\nPrimeras rutas de plugins:")
    for ruta in nuke.pluginPath()[:8]:
        print("  ", ruta)
    return 0


if __name__ == "__main__":
    main()
