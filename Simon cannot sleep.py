import math
h,m = map(int,input().split(":"))
temp = h*60*60 + m*60
a = 0
d = 3927.272727272727

ans = temp/d + 1
print(math.floor(ans))
