# C1. Given a string, find the second most frequent vowel letter
# 두 번째로 많이 사용한 모음 찾기

test = 'abcdeeeooauiea'
# test = 'abcdeeeooauieaaa'
vowel = 'aeiouAEIOU'


test = list(test)
check = []

for i in vowel:
    check.append((i, test.count(i)))

check.sort(key=lambda x: (x[1]))

print(''.join(test), ' -> ', check[len(check)-2][0])


