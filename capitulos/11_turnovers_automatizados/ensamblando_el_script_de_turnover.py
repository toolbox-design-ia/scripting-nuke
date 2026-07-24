def run_turnover(project_path, sequence_name, preset_name, output_dir):
    project = hiero.core.openProject(project_path)
    sequence = next(
        s for s in project.sequences() if s.name() == sequence_name
    )

    # Pre-flight
    media_errors = check_media_accessible(sequence)
    fps_errors = check_framerate_consistency(sequence)
    if media_errors or fps_errors:
        return {
            "status": "preflight_failed",
            "errors": media_errors + fps_errors
        }

    # Exportación
    start = datetime.datetime.utcnow()
    export_result = export_with_retry(sequence, preset_name)
    if export_result is not True:
        return {"status": "export_failed", "details": export_result}

    # Verificación
    expected = build_expected_paths(sequence, preset_name, output_dir)
    verification = verify_output_files(expected)

    # Reporte
    report = generate_turnover_report(
        sequence_name, preset_name, verification, start
    )
    report_path = os.path.join(
        output_dir, f"turnover_report_{sequence_name}.json"
    )
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    return report
