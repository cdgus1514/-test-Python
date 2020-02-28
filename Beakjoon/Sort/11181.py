# 단어정렬

# 길이가 짧은것 부터 우선정렬 >> 길이가 같으면 사전 순으로

# input data
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours


# 단어 개수 입력
n = int(input())

words = []
for i in range(n):
    word = input()
    length = int(len(word))

    words.append((word, length))

## 리스트 중복제거
words = list(set(words))
# print(words, end='\n\n')

## 정렬
words.sort(key=lambda x: (x[1], x[0]))

## 출력
for i in range(len(words)):
    print(words[i][0])