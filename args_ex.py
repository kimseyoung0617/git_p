def foo(*args):
    print(args)
    for item in args:
        print(item)

foo(10, 20, 30)
nums = [1, 2, 3]
foo(*nums)
