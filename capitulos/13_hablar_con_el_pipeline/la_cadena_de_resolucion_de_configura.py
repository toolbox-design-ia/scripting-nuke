import os, json
from pathlib import Path

def resolve_project_root(explicit_value=None):
    if explicit_value is not None:
        return explicit_value

    from_env = os.environ.get('PROJECT_ROOT')
    if from_env:
        return from_env

    config_path = Path.home() / '.studio_config.json'
    if config_path.exists():
        config = json.loads(config_path.read_text())
        if 'project_root' in config:
            return config['project_root']

    raise EnvironmentError(
        "PROJECT_ROOT no está definida. "
        "Establece la variable de entorno o pásala como argumento."
    )
