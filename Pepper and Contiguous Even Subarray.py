t= int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    c=0
    x=[-1]
    for i in range(n):
        if l[i]%2==0:
            c+=1
            x.append(c)
        else:
            c=0
    print(max(x))
