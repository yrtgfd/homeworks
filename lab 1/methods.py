python = int(input())
for attr in dir(python):
    if not attr.startswith('_'):
        print(attr)