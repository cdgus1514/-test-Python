# 단어공부

word = input()
test = list(word.lower())
test1 = set(test)

# 알파벳 개수 카운트
result = dict()
for i in test1:
    result[i] = test.count(i)

max_list = list()
# 가장 많은 알파벳 찾기
for k, v in result.items():
    if v == max(result.values()):
        max_list.append(str(k))

if len(max_list) > 1:
    print('?')
else:
    print(str(max_list[0]).upper())