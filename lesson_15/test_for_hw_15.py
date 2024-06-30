"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import unittest
from homework_15 import log_event

class TestLoginSystem(unittest.TestCase):

    # def setUp(self):
    #     # Очищення лог-файлу перед кожним тестом
    #     with open('login_system.log', 'w'):
    #         pass

    def test_successful_login(self):
        log_event('karyna_tashchi', 'success')
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Login event - Username: karyna_tashchi, Status: success', log_content)

    def test_expired_login(self):
        log_event('karyna_tashchi', 'expired')
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Login event - Username: karyna_tashchi, Status: expired', log_content)

    def test_failed_login(self):
        log_event('karyna_tashchi', 'failed')
        with open('login_system.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn('Login event - Username: karyna_tashchi, Status: failed', log_content)

if __name__ == "__main__":
    unittest.main(verbosity=2)
