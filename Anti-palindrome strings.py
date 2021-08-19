# Simple Solution First sort the string if sorted string is palindrome then print (-1) else print the sorted string. Because if the sorted string is palindrome then 
# the string will be something like this aaaaaa,bbbbb,ccccc,etc

# Write your code here
t = int(input())
for _ in range(t):
    inp = input()
    s = ''.join(sorted(inp))
    if s == s[::-1]:
        print(-1)
    else:
        print(s)
