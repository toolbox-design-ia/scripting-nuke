# Ejemplos listos para ejecutar

Pégalos en el **Script Editor** de Nuke (pestaña inferior) o cárgalos con
`nuke.scriptSource()`. Ninguno modifica el script sin avisar.

| Archivo | Qué hace | Escribe algo |
| --- | --- | --- |
| `00_comprobar_entorno.py` | Versión de Nuke, rutas de plugins y NUKE_PATH | No |
| `01_inventario_de_reads.py` | Lista los Read, su rango y marca los que apuntan a archivos que faltan | No |
| `02_renombrar_writes.py` | Aplica convención de nombres a los Write | Solo con `aplicar=True` |
| `03_panel_minimo.py` | Panel PySide acoplable de una sola acción | No |
