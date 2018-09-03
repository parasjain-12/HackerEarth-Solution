from collections import Counter
# Write your code here
def cc(a,b):
    p = Counter(a)
    q = Counter(b)
    print(sum((q-p).values())+sum((p-q).values()))



n  = int(input())
for _ in range(n):
    a = input()
    b = input()
    cc(a,b)
