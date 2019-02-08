t = int(input())
word  = 'SUVO'
word1 = 'SUVOJIT'
for _ in range(t):
    s = input()
    c = s.count(word)
    c2 = s.count(word1)
    print('SUVO = {}, SUVOJIT = {}'.format(c-c2,c2))
