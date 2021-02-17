n = int(input())
s = list(input().split())

half = n/2
x = []
for i in range(n):
    if i < half:
        x.append(s[i][0])
    else:
        x.append(s[i][-1:])

temp = ''.join(x)

if (int(temp) % 11 == 0):
    print("OUI")
else:
    print("NON")
