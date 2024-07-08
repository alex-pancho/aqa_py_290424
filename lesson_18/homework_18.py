### Завдання:

"""Розгляньте наступну функцію, яка обчислює факторіал числа:

```python
def factorial(n):
    Обчислює факторіал числа n.
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

Ваша мета полягає у створенні генератора, який буде генерувати послідовність факторіалів для чисел від 0 до n (включно). Також, застосуйте декоратор, який логує кожен виклик функції та виводить результат обчислення факторіалу.

### Вимоги:

1. Напишіть генератор `factorial_generator`, який приймає число n та генерує факторіали від 0 до n.

2. Напишіть декоратор `log_factorial_calls`, який логує (виводить у консоль) інформацію про кожен виклик функції, включаючи вхідні параметри та результат.

3. Застосуйте декоратор до функції `factorial`.

4. Створіть генератор та використайте його для генерації факторіалів для числа 5.

5. Запустіть програму та перевірте, чи логується правильна інформація.

6. Створити ПР з вашого бренча/форка

7. Дати посилання на ПР у форму відповіді

### Очікуваний результат:

```
Calling factorial(0)
Result: 1
Calling factorial(1)
Result: 1
Calling factorial(2)
Result: 2
Calling factorial(3)
Result: 6
Calling factorial(4)
Result: 24
Calling factorial(5)
Result: 120
```

Ваш код повинен логувати кожен виклик функції та виводити вхідні параметри та результат обчислення факторіалу.
"""

def log_factorial_calls(func):
    def wrapper(n):
        print(f"Calling factorial({n})")
        result = func(n)
        print(f"Result: {result}")
        return result
    return wrapper
@log_factorial_calls
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def factorial_generator(n):
    for i in range(n + 1):
        yield factorial(i)
for value in factorial_generator(5):
    pass




