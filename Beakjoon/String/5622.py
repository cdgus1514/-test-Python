# 다이얼


dial = ['abc', 'def', 'ghi', 'jkl', 'nmo', 'pqrs', 'tuv', 'wxyz']
time = 0

s = input().lower()

for i in range(len(s)):
    for j in dial:
        if s[i] in j:
            time += dial.index(j) + 3

print(time)