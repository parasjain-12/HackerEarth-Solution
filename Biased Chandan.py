n = int(input())
x=[]
for i in range(n):
    inq = int(input())
    if inq == 0:
        if len(x)>0:
            x.pop()
    else:
        x.append(inq)
print(sum(x))
