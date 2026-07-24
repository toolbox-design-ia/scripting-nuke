import nuke
import nukescripts

def launch_shot_panel():
    project_path = nuke.Root()["project_directory"].evaluate()
    repo = ShotRepository(project_path)
    panel = ShotPanel(repo)
    panel.setWindowTitle("Panel de shots")
    panel.resize(900, 500)
    panel.show()

nuke.menu("Nuke").addCommand(
    "Studio35/Panel de shots",
    launch_shot_panel,
    "ctrl+shift+p"
)
