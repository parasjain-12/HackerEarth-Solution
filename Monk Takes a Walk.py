t = int(input())
for _ in range(t):
    s = input()
    s = s.lower()
    c=0
    for i in range(len(s)):
        
        if s[i] =='a' or s[i] =='e' or s[i] =='i' or s[i] =='o' or s[i] =='u':
            c+=1
    print(c)
