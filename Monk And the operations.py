def abs_sum(row):
    s =0
    for i in range(len(row)):
        s += abs(row[i])
    return s
    
def abs_add(row,v1):
    l = len(row)
    for i in range(l):
        row[i] += v1
    x = abs_sum(row)
    return x
    

n,m= map(int,input().split())

#input Matrix
matrix = []
for i in range(n):
    a = list(map(int,input().split()))
    matrix.append(a)

v1,v2,v3,v4 = map(int,input().split())

#convert n rows into n column
col =[]
for i in range(m):
    a = []
    for j in range(n):
        a.append(matrix[j][i])
    col.append(a)

#row sum and update check   
f_sum1=0
for i in range(n):
    sum1=abs_sum(matrix[i])
    x=0
    temp = abs_add(matrix[i],v1)
    temp_2 = abs(len(matrix[i])*v2)
    if temp< temp_2:
        x = temp_2
    else:
        x = temp
    if x>sum1:
        sum1 = x
        
    #print(sum1,i)
    f_sum1 += sum1
    
c_sum1=0
for i in range(m):
    sum1=abs_sum(col[i])
    x12 = 0
    temp = abs_add(col[i],v3)
    temp_1 = abs(len(col[i])*v4)
    if temp< temp_1:
        x12= temp_1
    else:
        x12 = temp
        
    if x12>sum1:
        sum1 =x12
    #print(sum1,i)
    c_sum1 += sum1
    
if c_sum1>f_sum1:
    print(c_sum1)
else:
    print(f_sum1)
