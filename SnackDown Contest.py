t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    
    p= p[1:]
    q = q[1:]
    z = p+q
    z1 = list(set(z))
    
    if len(z1)==n:
        print('YES')
    else:
        print('NO')
