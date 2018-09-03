testCase = int(input())
for _ in range(testCase):
    n = int(input())
    l = list(map(int,input().split()))
    mi = []
    ma = []
    for i in range(n):
        ma.append(l[i]+i)
        mi.append(l[i]-i)
    print(max((max(mi)-min(mi)),(max(ma)-min(ma))))
