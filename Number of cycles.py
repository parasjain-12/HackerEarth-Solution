#Simple Cycles - No.of closed figure . 
#Hint - See Pattern

# Write your code here
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 1
    ans += (n-1)*n
    print(ans)
