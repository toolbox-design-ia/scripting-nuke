seq = project.sequences()[0]

for track in seq.videoTracks():
    for item in track.items():
        clip = item.source()
        print(
            item.name(),          # Nombre del shot (editable)
            item.timelineIn(),    # Frame de entrada en la timeline
            item.timelineOut(),   # Frame de salida en la timeline
            clip.source().filename()  # Ruta en disco
        )
