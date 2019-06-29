
T = int(input())
m = pow(10,9)+7
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    s=0
    ch= int(pow(2,N)//2)
    for i in range(N):
        if A[i]>=ch:
            s+=A[i]
    print(s%m)
