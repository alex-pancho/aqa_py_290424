def factorial(n):
    """Обчислює факторіал числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 1. Генератор factorial_generator
def factorial_generator(n):
    """Генератор факторіалів від 0 до n."""
    for i in range(n + 1):
        yield factorial(i)


# 2. Декоратор log_factorial_calls
def log_factorial_calls(func):
    """Декоратор, що логує виклики функції."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({', '.join(map(str, args))})")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


# 3. Застосування декоратору до функції factorial
@log_factorial_calls
def factorial(n):
    """Обчислює факторіал числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == '__main__':
    # 4. Створення генератора та використання його для генерації факторіалів для числа 5
    gen = factorial_generator(5)
    for fact in gen:
        pass
