import hiero.core

def export_sequence(sequence, preset_name):
    registry = hiero.core.taskRegistry()
    preset = None
    for p in registry.exportPresets():
        if p.name() == preset_name:
            preset = p
            break

    if preset is None:
        raise ValueError(f"Preset '{preset_name}' no encontrado en la sesión.")

    export_items = [hiero.core.ItemWrapper(sequence)]
    hiero.core.export(export_items, preset)
