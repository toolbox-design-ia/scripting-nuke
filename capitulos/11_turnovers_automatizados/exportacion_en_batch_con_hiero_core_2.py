import time

def wait_for_export(timeout_seconds=3600):
    registry = hiero.core.taskRegistry()
    start = time.time()
    while True:
        active_tasks = registry.activeTasks()
        if not active_tasks:
            break
        if time.time() - start > timeout_seconds:
            raise TimeoutError("La exportación excedió el tiempo máximo permitido.")
        time.sleep(2)
