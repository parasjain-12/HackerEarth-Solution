a=int(input())
b=list(input().split())
max=0
for i in range(10):
    i=str(i)
    count=0
    for j in b:
        if(i in j):
            count=count+1
    if(count>max):
        max=count
print(max)
