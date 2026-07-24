import hiero.core
import hiero.exporters

# Construir el preset desde un archivo de configuración existente
preset = hiero.core.taskRegistry.createPresetFromXml(
    open("/pipeline/export_presets/ingest_v03.xml").read()
)

# Seleccionar los items a exportar
seq = hiero.core.projects()[0].sequences()[0]
items = []
for track in seq.videoTracks():
    items.extend(track.items())

# Lanzar el procesador
processor = hiero.core.taskRegistry.createProcessor(preset)
processor.startProcessing(items)
