n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
p=0
if n>m:
    for i in range(m):
        if a[i]<b[i]:
            p+=b[i]-a[i]
        else:
            break
else:
    for i in range(n):
        if a[i]<b[i]:	
            p+=b[i]-a[i]
        else:
            break
print(p)
