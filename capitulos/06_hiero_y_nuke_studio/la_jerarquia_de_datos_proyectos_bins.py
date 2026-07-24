import hiero.core

# Proyecto activo
project = hiero.core.projects()[0]

# Bins de nivel superior
for bin in project.bins():
    print(bin.name())

# Secuencias del proyecto
for seq in project.sequences():
    print(seq.name(), seq.duration())
