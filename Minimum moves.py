n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    if x<0 or y<0 or y>x:
        print(-1)
    else:
        print(max(x,y))
