t = int(input())
for _ in range(t):
    l,r,s = map(int,input().split())
    if s > r:
        print(-1,-1)
    else:
        mi = int(((l-1)/s) + 1)
        ma = r//s
        if mi>ma:
            print(-1,-1)
        else:
            print(mi,ma)
