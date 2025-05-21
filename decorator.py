def original():
    print('original function')

def decorator(func):
    def wrapper():
        print('>>> Before')
        func()
        print('>>> After')
    return wrapper

decorated = decorator(original)
decorated()

@decorator
def original2():
    print('original2 function')

original2()
