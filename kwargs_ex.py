def bar(**kwargs):
    print(kwargs)
    for key, val in kwrags.items():
        print(f'{key} = {val}')

bar(a=1, b=2, c=3)

options = {'x': 10, 'y': 20}
bar(**options)
