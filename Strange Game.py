testcase = int(input())
for _ in range(testcase):
    le,k = map(int,input().split())
    alice = list(map(int,input().split()))
    bob=list(map(int,input().split()))
    x = max(bob)+1
    t=0
    for i in range(le):
        if x-alice[i]>0:
            t += (x-alice[i])*k
    print(t)
