def stairs(price, step):
    if len(price) < step:
        return price[-1]
    else:
        for i, v in enumerate(price):
            if i < step:
                continue
            else:
                p = min(price[i-step:i])
                price[i] += p
        return price[-1]

price = [int(x) for x in input().split(', ')]
step = int(input())
print(stairs(price, step))