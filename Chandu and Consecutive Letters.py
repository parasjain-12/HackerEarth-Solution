n = int(input())
for i in range(n):
    s = input()
    st = []
    for i in range(len(s)):
        if len(st)==0:
            st.append(s[i])
        elif st[-1]==s[i]:
            pass
        else:
            st.append(s[i])
    print(''.join(st))
    
