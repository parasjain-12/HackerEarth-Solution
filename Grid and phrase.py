n,m = map(int,input().split())
matrix = []
for i in range(n):
    a= list(input())
    matrix.append(a)
c=0
#horizontal
for i in range(n):
        for j in range(m):
            if m-j>=4:
                #print(m,j,i)
                if matrix[i][j]=='s' and matrix[i][j+1]=='a' and matrix[i][j+2]=='b' and matrix[i][j+3]=='a':
                    #print("yes")
                    c+=1
                    
#Vertical
for j in range(m):
    #ro
    for i in range(n):
        if n-i>=4:
            
            if matrix[i][j]=='s' and matrix[i+1][j]=='a' and matrix[i+2][j]=='b' and matrix[i+3][j]=='a':
                c+=1
                
                

for i in range(n):
    for j in range(m):
        if n-i>=4 and m-j>=4:
            #print(i,j)
            #print(matrix[i][j], matrix[i+1][j+1], matrix[i+2][j+2], matrix[i+3][j+3])
            if matrix[i][j]=='s' and matrix[i+1][j+1]=='a' and matrix[i+2][j+2]=='b' and matrix[i+3][j+3]=='a':
                #print("yes")
                c+=1

for i in range(n-1,0,-1):
    for j in range(m):
        if i+1 >= 4 and m-j>=4:
            if matrix[i][j]=='s' and matrix[i-1][j+1]=='a' and matrix[i-2][j+2]=='b' and matrix[i-3][j+3]=='a':
                #print("ds")
                c+=1
                
                
                
print(c)
