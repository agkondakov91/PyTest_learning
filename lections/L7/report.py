from datetime import datetime


def get_current_year() -> int:
    """Возвращает текущий год."""
    return datetime.now().year


def generate_report_title(project_name: str) -> str:
    """Генерирует заголовок отчёта с текущим годом."""
    year = get_current_year()
    return f"Отчёт по проекту '{project_name}' за {year} год"
