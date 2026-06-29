# 🧪 Python Testing with pytest — учебный курс

![Tests](https://github.com/agkondakov91/PyTest_learning/actions/workflows/lint.yml/badge.svg)

Материалы курса по тестированию Python-кода с помощью pytest. Курс охватывает полный цикл: от понимания зачем писать тесты — до автоматического запуска в CI через GitHub Actions.

---

## 📚 Содержание курса

| # | Лекция                          | Тема                                                             |
|---|---------------------------------|------------------------------------------------------------------|
| 1 | Зачем писать тесты              | Мотивация, пирамида тестирования, TDD, pytest vs unittest        |
| 2 | Конфигурация pytest             | Структура проекта, `pyproject.toml`, первые тесты, паттерн AAA   |
| 3 | Флаги и маркеры                 | `-v`, `-k`, `-x`, `--tb`, `@pytest.mark.*`, регистрация маркеров |
| 4 | Юнит-тесты                      | Happy path, edge cases, error cases, `pytest.raises`             |
| 5 | Параметризация                  | `@pytest.mark.parametrize`, `ids`, `pytest.param`                |
| 6 | Фикстуры                        | `@pytest.fixture`, `yield`, скоупы, `conftest.py`                |
| 7 | Моки и патчинг                  | `unittest.mock`, `patch`, `monkeypatch`, проверка вызовов        |
| 8 | Интеграционные тесты + Django   | `pytest-django`, тесты моделей и views, тестовая БД              |
| 9 | Тестирование REST API + FastAPI | `TestClient`, `httpx2`, тесты эндпоинтов, коды 422/201/204       |
| 10 | Coverage                        | `pytest-cov`, HTML-отчёт, `--cov-fail-under`, `pragma: no cover` |
| 11 | CI: GitHub Actions              | workflow, jobs, `needs`, бейдж в README, автозапуск тестов       |

---

## 🛠️ Стек

- **Python 3.14+**
- **uv** — управление окружением и зависимостями
- **pytest** — основной фреймворк для тестирования
- **pytest-django** — интеграция с Django
- **httpx2** — HTTP-клиент для тестирования FastAPI
- **pytest-cov** — отчёты о покрытии кода
- **Ruff** — линтер и форматтер
- **pre-commit** — автоматические проверки перед коммитом
- **GitHub Actions** — автоматический запуск тестов в CI

---

## 🚀 Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone git@github.com:agkondakov91/PyTest_learning.git
cd PyTest_learning
```

### 2. Установить зависимости

Для управления зависимостями используется **uv**. Если он ещё не установлен:

```bash
# macOS / Linux
curl -Lsf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Проверка
uv --version
```

Устанавливаем зависимости проекта:

```bash
uv sync --dev
```

### 3. Подключить git-хуки

```bash
uv run pre-commit install
```

После этого Ruff будет запускаться автоматически перед каждым `git commit`.

### 4. Запустить тесты

```bash
uv run pytest
```

---

## 🔧 Полезные команды

### Запуск тестов

```bash
# Базовый запуск
uv run pytest

# Подробный вывод
uv run pytest -v

# Только конкретный файл
uv run pytest tests/test_cart.py

# Только конкретный тест
uv run pytest tests/test_cart.py::test_cart_total

# По имени теста
uv run pytest -k "discount"

# По маркеру
uv run pytest -m fast

# Остановиться при первом падении
uv run pytest -x

# Показывать print() в тестах
uv run pytest -s

# Тесты FastAPI (лекция 9 — запускать из папки лекции)
cd lections/L9
uv run pytest tests/test_api.py -v -p no:django
```

### Покрытие кода

```bash
# Отчёт в терминале с указанием непокрытых строк
uv run pytest --cov=src --cov-report=term-missing

# HTML-отчёт (открыть htmlcov/index.html)
uv run pytest --cov=src --cov-report=html

# Завершить с ошибкой если покрытие ниже 70%
uv run pytest --cov=src --cov-fail-under=70
```

### Линтер

```bash
# Проверить весь проект
uv run ruff check .

# Проверить и автоматически исправить
uv run ruff check --fix .

# Отформатировать код
uv run ruff format .
```

### Django (лекция 8)

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

### FastAPI (лекция 9)

```bash
cd lections/L9
uv run uvicorn api.main:app --reload
# Документация API: http://127.0.0.1:8000/docs
```

---

## ⚙️ Конфигурация

Все настройки хранятся в `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
python_classes = ["Test*"]
DJANGO_SETTINGS_MODULE = "config.settings"
markers = [
    "fast: быстрые тесты (без внешних зависимостей)",
    "slow: медленные тесты (база данных, сеть)",
    "smoke: базовые тесты для проверки работоспособности",
]

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/migrations/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if __name__ == .__main__.:",
]

[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "W", "F", "N", "I"]
ignore = ["E501"]
```

---

## 📂 Структура проекта

```bash
PyTest_learning/
├── .github/
│   └── workflows/
│       └── tests.yml              # CI-пайплайн
├── lections/
│   ├── L8/                        # Django (лекция 8)
│   │   ├── config/                # Django-конфигурация
│   │   ├── shop/                  # Django-приложение
│   │   ├── tests/
│   │   │   ├── conftest.py
│   │   │   ├── test_models.py
│   │   │   └── test_views.py
│   │   ├── db.sqlite3
│   │   └── manage.py
│   └── L9/                        # FastAPI (лекция 9)
│       ├── api/
│       │   ├── main.py
│       │   ├── models.py
│       │   └── storage.py
│       └── tests/
│           ├── conftest.py
│           └── test_api.py
├── src/                           # Основной код (лекции 1–7)
│   ├── __init__.py
│   ├── l1_example.py
│   ├── l2_calculator.py
│   ├── l4_order.py
│   ├── L3.md
│   ├── l5_discount.py
│   ├── l6_cart.py
│   ├── l7_notifications.py
│   ├── l7_report.py
│   └── l7_weather.py
├── tests/                         # Тесты (лекции 2–7)
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_l2_calculator.py
│   ├── test_l3_example.py
│   ├── test_l4_order.py
│   ├── test_l5_discount.py
│   ├── test_l6_cart.py
│   ├── test_l7_notifications.py
│   ├── test_l7_report.py
│   └── test_l7_weather.py
├── main.py
├── .gitignore
├── .pre-commit-config.yaml        # Хуки для git
├── .python-version
├── pyproject.toml                 # Настройки проекта
├── uv.lock
└── README.md
```

---

## 💡 Как работает защита кода

```
Локально                          На сервере
─────────────────────────         ──────────────────────────────
git commit                        git push / pull request
↓                                 ↓
pre-commit запускает Ruff         GitHub Actions запускает pytest
↓                                 ↓
Ошибки → коммит отменён           Ошибки → красный крест ✗
Всё чисто → коммит прошёл         Всё чисто → зелёная галочка ✓
```

---

## 📖 Полезные ссылки

- [Документация pytest](https://docs.pytest.org/)
- [pytest-django](https://pytest-django.readthedocs.io/)
- [Документация FastAPI](https://fastapi.tiangolo.com/)
- [Coverage.py](https://coverage.readthedocs.io/)
- [Документация uv](https://docs.astral.sh/uv/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Martin Fowler — Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)

---

## 👨‍🏫 Об авторе

Курс подготовлен для студентов, изучающих Python-разработку.  
Преподаватель: Александр / [agkondakov91](https://github.com/agkondakov91)