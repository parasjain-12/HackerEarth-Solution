n= int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [0]*n
for i in range(n):
    c[i] = a[i]+b[i]
print(*c)
