n = int(input())
s = input()
consecutive_house = []
temp = 0
arr = ['']*n
for i,j in enumerate(s):
    if j == 'H':
        arr[i] = 'H'
        temp += 1 
        if i == n-1:
            consecutive_house.append(temp)
    else:
        arr[i] = 'B'
        if temp > 0:
            consecutive_house.append(temp)
            temp = 0
            
if len(consecutive_house) == 0 or max(consecutive_house) == 1:
    print('YES')
    print(''.join(arr))
else:
    print('NO')
