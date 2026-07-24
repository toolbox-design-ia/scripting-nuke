from jinja2 import Template
from pathlib import Path

QC_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>QC Report - {{ session.project }}</title>
<style>
  body { font-family: monospace; background: #1a1a1a; color: #d4d4d4; }
  .fail { color: #ff6b6b; }
  .warn { color: #ffd93d; }
  .pass { color: #6bcb77; }
  table { border-collapse: collapse; width: 100%; }
  td, th { padding: 6px 12px; border: 1px solid #333; text-align: left; }
</style>
</head>
<body>
<h1>QC Ingest — {{ session.project }}</h1>
<p>{{ session.timestamp }} | {{ session.total }} clips |
   <span class="fail">{{ session.failed }} FAIL</span> |
   <span class="warn">{{ session.warned }} WARN</span> |
   <span class="pass">{{ session.passed }} PASS</span></p>
{% for clip in clips %}
<h2 class="{{ clip.verdict.lower() }}">{{ clip.verdict }} — {{ clip.clip }}</h2>
<table>
{% for check in clip.checks %}
<tr class="{{ 'fail' if not check.passed and check.severity == 'critical' else 'warn' if not check.passed else 'pass' }}">
  <td>{{ check.rule }}</td>
  <td>{{ check.message or 'OK' }}</td>
</tr>
{% endfor %}
</table>
{% endfor %}
</body>
</html>
"""

def render_html_report(session_data: dict) -> str:
    template = Template(QC_TEMPLATE)
    return template.render(**session_data)
