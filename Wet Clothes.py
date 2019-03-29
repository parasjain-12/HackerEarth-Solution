n,m,g = input().split()
t = list(map(int,input().split()))
a = list(map(int,input().split()))
gap =[]
for i in range(len(t)-1):
    x = t[i+1]-t[i]
    gap.append(x)
    
m = max(gap)
c=0
for i in range(len(a)):
    if a[i]<=m:
        c+=1
print(c)
