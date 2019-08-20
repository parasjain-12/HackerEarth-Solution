from collections import Counter
n= int(input())
a = list(map(int,input().split()))
m = int(input())
p = Counter(a)
for i in range(m):
    x = int(input())
    if p[x]:
        print(p[x])
    else:
        print('NOT PRESENT')
