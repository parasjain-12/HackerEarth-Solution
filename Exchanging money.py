import math

n,q = map(int,input().split())
arr = list(map(int,input().split()))

g= arr[0]
for i in range(n):
    g = math.gcd(g,arr[i])
    
for i in range(q):
    q1 = int(input())
    if q1%g==0:
        print("YES")
    else:
        print("NO")
