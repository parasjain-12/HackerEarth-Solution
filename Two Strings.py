from collections import Counter
def check(a,b):
    p = Counter(a)
    q = Counter(b)
    if sum((p-q).values())==0:
        print('YES')
    else:
        print('NO')


n = int(input())
for _ in range(n):
    a,b = input().split()
    check(a,b)
