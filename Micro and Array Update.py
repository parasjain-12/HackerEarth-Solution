n= int(input())
for _ in range(n):
    le,k  = map(int,input().split())
    array = list(map(int,input().split()))
    x = k-min(array)
    if x>0:
        print(x)
    else:
        print(0)
