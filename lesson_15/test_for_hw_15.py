"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import pytest
import os
from homework_15 import log_event


# Фикстура. Получаем доступ к лог файлу, который тестируем.
@pytest.fixture(scope='module')
def log_file_path():
    # Получаем путь к папке, где находится данный файл (lesson_15)
    current_dir = os.path.dirname(__file__)
    # Получаем путь к лог файлу, который находится на уровень выше папки lesson_15
    return os.path.abspath(os.path.join(current_dir, '..', 'login_system.log'))


# Фикстура. Очищает лог файл перед каждым тестом
@pytest.fixture(autouse=True)
def setup_clear_log_file(log_file_path):
    # Очищаем файл, если он существует
    if os.path.exists(log_file_path):
        with open(log_file_path, 'w'):
            pass


def test_successful_login(log_file_path):
    # Вызов функции для записи события логина
    log_event('serhii', 'success')
    # Проверка содержимого лог-файла
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        log_content = log_file.read()
        assert 'Login event - Username: serhii, Status: success' in log_content


def test_expired_login(log_file_path):
    # Вызов функции для записи события логина
    log_event('ihor', 'expired')
    # Проверка содержимого лог-файла
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        log_content = log_file.read()
        assert 'Login event - Username: ihor, Status: expired' in log_content


def test_failed_login(log_file_path):
    # Вызов функции для записи события логина
    log_event('denys', 'failed')
    # Проверка содержимого лог-файла
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        log_content = log_file.read()
        assert 'Login event - Username: denys, Status: failed' in log_content


if __name__ == "__main__":
    pytest.main()
