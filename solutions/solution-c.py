n, b, s = map(int, input().split())

cache = {}

def count_numbers(n, s, birinchi_son):
    key = (n, s, birinchi_son)
    if key in cache:
        return cache[key]
    
    if n == 1:
        if birinchi_son:
            cache[key] = 1 if (1 <= s < b) else 0
        else:
            cache[key] = 1 if (0 <= s < b) else 0
        return cache[key]
    
    res = 0
    start = 1 if birinchi_son else 0
    for d in range(start, b):
        if s - d >= 0:
            res += count_numbers(n - 1, s - d, False)
    
    cache[key] = res
    return res

print(count_numbers(n, s, True))