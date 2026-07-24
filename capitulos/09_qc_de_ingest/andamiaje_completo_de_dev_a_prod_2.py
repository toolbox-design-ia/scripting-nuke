# hiero_qc_panel.py — registra el panel en el menú de Hiero
import hiero.core
import hiero.ui
from qc_ingest import run_qc_session

def run_qc_on_selection():
    clips = hiero.ui.activeView().selection()
    paths = [c.mediaSource().fileinfos()[0].filename() for c in clips]
    results = run_qc_session(paths, spec_path="specs/project_spec.json")
    report_html = render_html_report(results)
    # Abrir reporte en navegador del sistema.
    import webbrowser, tempfile
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as f:
        f.write(report_html)
        webbrowser.open(f.name)

action = hiero.ui.createMenuAction("QC Ingest Selection", run_qc_on_selection)
hiero.ui.findMenuAction("foundry.menu.sequence").menu().addAction(action)
