n = int(input())
for i in range(n):
    first_word = input()
    second_word = input()
    for i in second_word:
        if i in first_word:
            print("YES")
            break
    else:
        print("NO")
