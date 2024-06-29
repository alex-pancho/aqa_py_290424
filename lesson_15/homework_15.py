"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import os


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    # Сообщение, которое укажем в логе
    log_message = f"Login event - Username: {username}, Status: {status}"
    # Получаем путь к папке, где находится данный файл (lesson_15)
    current_dir = os.path.dirname(__file__)
    # Получаем путь к лог файлу, который находится на уровень выше папки lesson_15
    log_file = os.path.abspath(os.path.join(current_dir, '..', 'login_system.log'))

    # Создание и настройка логера
    logger = logging.getLogger("log_event")
    logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования

    # Создаем обработчик для записи в файл
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)  # Устанавливаем уровень логирования для обработчика

    # Создаем форматтер и добавляем его к обработчику
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Удаляем все предыдущие обработчики (чтобы избежать дублирования)
    logger.handlers = []

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


log_event('serhii', 'success')
log_event('ihor', 'expired')
log_event('denys', 'failed')
