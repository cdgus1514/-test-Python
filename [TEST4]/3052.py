#나머지

#result = [0 for _ in range(10)]
result = []
num = []
cnt = 0

# 데이터 입력
for i in range(10):
    n = int(input(">> "))

    if 0 < n and n <= 1000:
        num.append(n)


# 나머지 값 입력
for i in range(10):
    div = (num[i] % 42);
    result.append(div)


result2 = result

# 나머지 비교
'''
for i in range(10):
    for j in range(10):
        if j == i:
            pass

        if result[i] in result2[j]:
            pass
        else:
            cnt+=1
'''

result2 = set(result)



print(num)
print(result)

print(len(result2))