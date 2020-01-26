n = int(input())
arr = list(map(int,input().split()))
ma = max(arr)
mi = min(arr)

s = sum(arr)

a1_max = s-mi
a2_min = s-ma
print(a2_min,a1_max)
