def find(a):
    ch = a%12
    if ch==1:
        print(a+11,'WS')
    elif ch==0:
        print(a-11,'WS')
    elif ch==6:
        print(a+1,'WS')
    elif ch==7:
        print(a-1,'WS')

        
    elif ch==2:
        print(a+9,'MS')
    elif ch==3:
        print(a+7,'AS')
    elif ch==4:
        print(a+5,'AS')
    elif ch==5:
        print(a+3,'MS')
    elif ch==8:
        print(a-3,'MS')
    elif ch==9:
        print(a-5,'AS')
    elif ch==10:
        print(a-7,'AS')
    else:
        print(a-9,'MS')


n = int(input())
for i in range(n):
    a = int(input())
    find(a)
