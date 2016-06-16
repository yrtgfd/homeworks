import operator

a = input()
try:
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = []
    for token in a.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1, op2))
        elif token:
            stack.append(float(token))
    if len(stack) == 1:
        print(stack.pop())
    else:
        print('ERROR')
except:
    print('ERROR')