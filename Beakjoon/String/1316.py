# 그룹 단어 체커

## find 함수를 사용해서 각 글자를 인덱스로 바꿔 두 글자씩 비교
## 앞 글자가 처음 등장하는 인덱스보다, 뒷 글자가 처음 등장하는 인덱스보다 작으면 뒷글자는 이미 등장한 글자

num = int(input())


for _ in range(num):
    word = input()

    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]):
            num -= 1
            break

print(num)


'''
4

aba
0 1
1 0
abab
0 1
1 0
abcabc
0 1
1 2
2 0
a
1
'''