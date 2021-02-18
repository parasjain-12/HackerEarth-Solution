d = {}
n = input()
s = 'abcdefghijklmnopqrstuvwxyz'
for i,j in enumerate(s):
    d[j] = i+1
cost = 0
for i in n:
    cost += d[i]

print(cost)
