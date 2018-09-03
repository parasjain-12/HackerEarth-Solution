n,k = map(int,input().split())
l = list(map(int,input().split()))
c=0
skip=0
for i in range(n):
    if l[i]<=k and skip<2:
        #print(l[i])
        c+=1
    else:
        skip+=1
print(c)
