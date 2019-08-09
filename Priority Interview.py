n = int(input())

x_y = []
for i in range(n):
    a,b = map(int,input().split())
    x_y.append([a,b])
x_y.sort(key = lambda x : x[1],reverse = True)
x_y.sort(key = lambda x : x[0])

for i in range(len(x_y)):
    print(x_y[i][1],end = ' ')
