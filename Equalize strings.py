n = int(input())
x = input()
y = input()
c = 0
l = 0
for i in range(n):
    if x[i] != y[i]:
        c+=1
    else:
        if c > 0:
            l += 1
            c =0
if c >0:
    l+=1
    
print(l)
