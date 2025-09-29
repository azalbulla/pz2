import time
from functools import wraps

def timer(func):
    """Декоратор для измерения времени выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func.__name__} выполнена за {end - start:.4f} сек.")
        return result
    return wrapper

def logger(func):
    """Декоратор для логирования вызовов функций."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершилась.")
        return result
    return wrapper

def repeater(repeats=1):
    """Декоратор для повторного выполнения функции."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(repeats):
                print(f"Повтор {i+1}/{repeats}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator