n = int(input())
for _ in range(n):
    s = list(input())
    op = ["{","[","("]
    cl = ["}","]",")"]
    
    st = [s[0]]
    for i in range(1,len(s)):
        if st:
            temp =s[i]
            if temp in op:
                st.append(temp)
            else:
                ind = cl.index(s[i])
                if st[-1]==op[ind]:
                    st.pop()
        else:
            st.append(s[i])
    if len(st)>0:
        print("NO")
    else:
        print("YES")
