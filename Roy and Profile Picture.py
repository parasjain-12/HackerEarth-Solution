l  = int(input())
t = int(input())
for _ in  range(t):
    m,n = map(int,input().split())
    if m < l or n<l:
        print("UPLOAD ANOTHER")
    elif m==n:
        print("ACCEPTED")
    else:
        print("CROP IT")
