n = int(input())
l = list(map(int,input().split()))



for i in range(n-1):
    if l[i]<=l[i+1]:
        l[i+1] = l[i+1]-l[i]
    else:
        print('NO')
        break
else:
    if l[n-1]==0:
        print('YES')
    else:
        print('NO')
