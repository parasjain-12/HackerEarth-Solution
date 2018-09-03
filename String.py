from collections import Counter
n = int(input())
st = input()
p = Counter(st)
print(n - max(p.values()))
