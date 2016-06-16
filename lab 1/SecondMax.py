def get_secnd_max(arr):
    try:
        return max(a for a in arr if a != max(arr))
    except:
        return 'NO'
a = [int(x) for x in input().split(' ')]
print(get_secnd_max(a))