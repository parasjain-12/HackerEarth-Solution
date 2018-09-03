n,m= map(int,input().split())
l = list(map(int,input().split()))
x=[]
for i in range(0,n):
    if len(l[i:m+i])==m:
        x.append(max(l[i:m+i]))
print(*x)
