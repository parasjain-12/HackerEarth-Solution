'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
mi = min(a)
i = 0
while i <n:
    if a[i]>=b[i]:
        while a[i]>mi:
            a[i] -= b[i]
            count+=1
    if a[i] < mi:
            mi = a[i]
            i = 0
    if a[i] != mi:
        count = -1
        break
    i+=1 

print(count)

#A rare test case :
#         n=2
#        a = [3,2]
#        b = [2,1]
# then all a's element should be 1
