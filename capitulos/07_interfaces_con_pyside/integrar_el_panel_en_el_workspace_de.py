import nuke
import nukescripts

class PanelFiltroReads(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(
            self,
            "Filtro de Reads",
            "studio35.filtro_reads"
        )
        self.patron_knob = nuke.String_Knob("patron", "Patrón de path")
        self.addKnob(self.patron_knob)

        self.ejecutar_knob = nuke.PyScript_Knob(
            "ejecutar", "Filtrar",
            "import herramientas.filtro; herramientas.filtro.ejecutar()"
        )
        self.addKnob(self.ejecutar_knob)

def registrar_panel():
    nukescripts.registerPanel(
        "studio35.filtro_reads",
        lambda: PanelFiltroReads()
    )
