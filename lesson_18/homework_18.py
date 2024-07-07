import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_factorial_calls(func):
    def wrapper(n):
        logging.info(f"Calling {func.__name__}({n})")
        result = func(n)
        logging.info(f"Result: {result}")
        return result
    return wrapper

@log_factorial_calls
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result= result*i
    return result

def factorial_generator(n):
    for i in range(n + 1):
        yield factorial(i)


for fact in factorial_generator(5):
    pass