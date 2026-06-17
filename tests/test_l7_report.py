from unittest.mock import MagicMock, patch

import lections.L7.report as report_module
from lections.L7.report import generate_report_title


@patch("lections.L7.report.get_current_year")
def test_generate_report_title(mock_year: MagicMock):
    mock_year.return_value = 2026
    result = generate_report_title("Testing")
    assert result == "Отчёт по проекту 'Testing' за 2026 год"


def test_report_title_with_monkeypatch(monkeypatch):
    monkeypatch.setattr(report_module, "get_current_year", lambda: 2025)
    result = generate_report_title("Pytest")
    assert result == "Отчёт по проекту 'Pytest' за 2025 год"
