'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def getSum(n):
    su = 0
    while n!=0:
        rem = n%10
        su += rem
        n = n//10
        
    return su

n = int(input())
li = []
for i in range(n):
    x = int(input())
    for i in range(x,10000000000):
        su = getSum(i)
        if su%4 == 0:
            print(i)
            break
