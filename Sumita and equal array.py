t = int(input())
for _ in range(t):
    n,x,y,z = map(int,input().split())
    l = list(map(int,input().split()))
    for i in range(n):
        while l[i]%x==0:
            l[i] = l[i]/x
        while l[i]%y==0:
            l[i] = l[i]/y
        while l[i]%z==0:
            l[i] = l[i]/z
    for i in range(1,n):
        if l[i]!=l[i-1]:
            print("She can't")
            break
    else:
        print('She can')
