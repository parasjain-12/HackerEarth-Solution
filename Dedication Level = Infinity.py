n= int(input())
l = [[0 for i in range(2)]for i in range(n)]
for i in range(n):
    l[i] = list(input().split())
for i in range(n):
    l[i][1]  = int(l[i][1])
l.sort(key = lambda x:x[1],reverse = True)
for i in range(3):
    print(l[i][0])
