'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n,m = map(int,input().split())
lis = []
for i in range(n):
    temp = list(map(int,input().split()))
    lis.append(temp)

mx = [0]*m
su = [0]*n
for i in range(n):
    for j in range(m):
        mx[j] = max(mx[j],lis[i][j])
        su[i] += lis[i][j]


cn = [0]*n
goodNumber = 0
for i in range(n):
    for j in range(m):
        if mx[j] == lis[i][j]:
            cn[i]+=1
        goodNumber = max(goodNumber,cn[i])


index = []
for i in range(len(cn)):
    if goodNumber == cn[i]:
        index.append(i)

ansSum = 0
ansIndex = 0
if len(index)>1:
    for i in range(len(index)):
        temp = su[index[i]]/4
        if temp>ansSum:
            ansSum = temp
            ansIndex = index[i]

    print(ansIndex+1)

else:
    print(index[0]+1)
