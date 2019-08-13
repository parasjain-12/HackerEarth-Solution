s = input()

op = '('
cl = ')'
st = [s[0]]
for i in range(1,len(s)):
    #print(st)
    if st:
        temp =s[i]
        if temp == cl:
            
            if op == st[-1]:
                st.pop()
                
            else:
                st.append(s[i])
        else:
            st.append(s[i])
    else:
        st.append(s[i])

print(len(st))
