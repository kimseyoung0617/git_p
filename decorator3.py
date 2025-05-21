def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
            return wrapper
        return decorator

@repeat(3)
def hello(name):
    print(f'Hello, {name}!')

hello('Alice')
