s = input()
stack = [s[0]]
for i in range(1,len(s)):
    if stack:
        
        if stack[-1]== s[i]:
            #print("ssds",stack)
            stack.pop()
        else:
            stack.append(s[i])
    else:

        stack.append(s[i])
    #stack.append(s[i])
if len(stack)>0:
    print(''.join(stack))
else:
    print('Empty String')
