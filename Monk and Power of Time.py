n = int(input())

cal = list(map(int,input().split()))
ide = list(map(int,input().split()))
j=0
t=0
while(j!=n):
    #print('xxx')
    if (cal[0] == ide[0]):
        t+=1
        x=cal.pop(0)
        y = ide.pop(0)
        j+=1
    else:
        x = cal.pop(0)
        cal.append(x)
        #print(cal)
        t+=1
print(t)
