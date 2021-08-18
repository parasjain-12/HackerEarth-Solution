#Step 1 : We first find out the powers of numbes smaller than or equal to x.Eg x = 91 ,k = 3 so we first find out [1,3,9,27,81]
#Step 2 : We start a loop and subtract the largest number one by one from x and simulatensly check whether they are equal or not.
#Step 3 : If they are equal print - YES else NO

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for _ in range(t):
    x,k = map(int,input().split())
    options = [1]
    val = k
    count = 1
    while val<=x:
        count+=1
        options.append(val)
        val = k**count
        
    total = options.pop()

    while total <= x:
        dif = x - total
        options = [i for i in options if i<= dif]
        try:
            total += options.pop()
        except:
            break

            
    if total == x:
        print("YES")
    else:
        print("NO")
