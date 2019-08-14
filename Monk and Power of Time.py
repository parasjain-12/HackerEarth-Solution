n = int(input())
call = list(map(int,input().split()))
ideal = list(map(int,input().split()))

def check(a,b):
    if a[0] == b[0]:
        return True
    return False

c=0
while len(call)>0:
    if check(call,ideal)==True:
        call = call[1:]
        ideal = ideal[1:]
        c+=1
    else:
        call = call[1:n]+call[:1]
        #print(call)
        c+=1

print(c)
