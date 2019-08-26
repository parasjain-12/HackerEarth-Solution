n,m= map(int,input().split())
from collections import Counter
arr = list(map(int,input().split()))
d = Counter(arr)


flag = 0
for i in range(n):
    temp = m - arr[i]
    if d[temp]:
        if arr[i]==temp and d[temp]==1:
            continue
        print("YES")
        flag = 1
        break
if flag==0:
    
    print("NO")
