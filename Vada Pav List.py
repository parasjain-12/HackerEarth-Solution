n = int(input())
l = []
for i in range(n):
    x = input()
    l.append(x)

l = list(set(l))
l.sort()
print(len(l))
for i in range(len(l)):
    print(l[i])
