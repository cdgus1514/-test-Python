# 알파벳 찾기

import string

# s = 'baekjoon'

word = input()
test = list(word)
result = dict()

for i in string.ascii_lowercase:
    result[i] = '-1'

for i in test:
    result[i] = str(test.index(i))

answer = list(result.values())
answer = ' '.join(answer)
print(answer)

'''
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
'''