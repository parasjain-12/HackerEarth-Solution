from collections import Counter,defaultdict
t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    d = defaultdict(int)
    d = Counter(arr)
    for _ in range(q):
        temp = int(input())
        print(d[temp])
