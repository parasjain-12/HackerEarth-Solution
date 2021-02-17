test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    s = input()
    count = 0

    for i in range(n-1):
        if s[i] != 'a' and s[i] != 'e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u' :
            if s[i+1] == 'a' or s[i+1] == 'e' or s[i+1] == 'i' or s[i+1] == 'o' or s[i+1] == 'u' :
                count += 1

    print(count)
