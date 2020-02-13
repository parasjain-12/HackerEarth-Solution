# Write your code here
import math
m,n = map(int,input().split())
x = math.gcd(m,n)
if x>1:
    print("Yes")
else:
    print("No")
