def get_rep_str_sub(s):
    n = len(s)
    i = 2
    k = 0
    while i < n:
        if n % i == 0 and n / i == s.count(s[:i]) and s.count(s[:i]) > k:
            k = s.count(s[:i])
            t = i
        i += 1
    return k

print(get_rep_str_sub(input()))