n = int(input())
a = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))
l=[]
for i in range(n):
    for j in range(m):
        x = c[j]-a[i]
        l.append(x)
    
from collections import Counter
l  = Counter(l)
ans = []
for k,v in l.items():
    if v==n:
        ans.append(k)
ans  =sorted(ans)
print(' '.join(map(str, ans)))
