test_case = int(input())
a = 0
b = 7
for i in range(test_case):
    f = int(input())
    temp = abs(f-a)
    temp2 = abs(f-b)
    if temp <= temp2:
        a = f
        print('A')
    else:
        b = f
        print('B')
