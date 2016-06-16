from itertools import product
from functools import reduce

numbers = input()
numbers = numbers.split(' ')
signs = ['+', '-']
combs = list(product(signs, repeat=len(numbers)-2))
flag = 0

for comb in combs:
    for i, number in enumerate(numbers[:-1]):
        a = list(comb[:])
        a.insert(i, '==')
        expression = ''.join(reduce(lambda x, y: x + y, zip(numbers, a))) + numbers[-1]
        if eval(expression):
            print('YES')
            flag = 1
            break
    if flag:
        break
else:
    print('NO')