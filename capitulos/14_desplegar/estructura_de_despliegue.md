# Estructura de despliegue impresa en el capitulo 14

```text
/tools/nuke/prod/
  init.py
  menu.py
  python/
    studio_io.py
    qc_panel.py
    color_utils.py
  gizmos/
    StudioRead.gizmo
    StudioWrite.gizmo
  plugins/
    StudioFormat.so        ← plugin compilado para Linux
    StudioFormat.dylib     ← plugin compilado para macOS
```
