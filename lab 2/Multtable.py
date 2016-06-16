def mult_table(m, n):
    p = len(str(m * n))
    n_length = len(str(n))
    for i in range(1, n + 1):
        print('{:_>{P}}_=_{:_>{K}}_{}'.format(i * m, i, m, P=p, K=n_length))

    return True

m, n = [int(i) for i in input().split(',')]
mult_table(m, n)