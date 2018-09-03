n  = int(input())
l = list(map(int,input().split()))[::-1]
pq = []
pq.append(l[0])
m = l[0]
for i in range(1,n):
    if l[i]>=m:
        pq.append(l[i])
        m=l[i]
print(*pq[::-1])
