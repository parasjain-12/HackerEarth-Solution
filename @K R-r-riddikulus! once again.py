n,d = map(int,input().split())
a = list(map(int,input().split()))
print(*(a[d:]+a[:d]))
#print(*(a[d:]+a[:d]))
