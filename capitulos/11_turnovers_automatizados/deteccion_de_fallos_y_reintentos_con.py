def export_with_retry(sequence, preset_name, max_retries=3):
    attempt = 0
    delay = 30
    while attempt < max_retries:
        try:
            export_sequence(sequence, preset_name)
            wait_for_export()
            failures = check_task_results()
            if not failures:
                return True
            if all("offline" in f.get("error", "").lower() for f in failures):
                attempt += 1
                time.sleep(delay)
                delay *= 2
                continue
            else:
                return failures
        except TimeoutError:
            attempt += 1
            time.sleep(delay)
            delay *= 2
    return False
