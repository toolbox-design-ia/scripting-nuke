import json
import datetime

def generate_turnover_report(sequence_name, preset_name, results, start_time):
    end_time = datetime.datetime.utcnow()
    return {
        "sequence": sequence_name,
        "preset": preset_name,
        "timestamp_start": start_time.isoformat(),
        "timestamp_end": end_time.isoformat(),
        "duration_seconds": (end_time - start_time).total_seconds(),
        "files": {
            "ok": results["ok"],
            "missing": results["missing"],
            "empty": results["empty"],
        },
        "status": "ok" if not results["missing"] and not results["empty"] else "failed"
    }
