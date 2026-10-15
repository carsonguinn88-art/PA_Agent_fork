import sys
with open("pa_agent/config/settings.py", "r") as f:
    content = f.read()
content = content.replace("<<<<<<< HEAD\n    context_warning_threshold_pct: float = 99_999_999.0\n    last_data_source: DataSourceKind = \"mt5\"\n=======\n    context_warning_threshold_pct: float = 80.0\n    last_data_source: DataSourceKind = \"tradingview\"\n>>>>>>> pr18", "    context_warning_threshold_pct: float = 99_999_999.0\n    last_data_source: DataSourceKind = \"mt5\"")
with open("pa_agent/config/settings.py", "w") as f:
    f.write(content)
