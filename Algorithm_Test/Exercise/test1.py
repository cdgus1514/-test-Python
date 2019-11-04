def solution(s):
    answer = ''

    if len(s) % 2 == 0:   # 짝수
        # print(s[start:end+1])
        print(s[(len(s)//2-1):(len(s)//2+1)])
    else:
        print(s[len(s) // 2])

    return answer


#################################
# s1 = 'abcde'
s1 = 'qwer'
# s1 = 'iuoiewrmcx'   # ew
# s1 = 'dasjflkjdsafoijcsvkjmlksdamfklsadfjmoisjadvniosadnvmndasfsdafdsf'  # 64 >> ad
# s1 = 'kdfajssdaoifjsdakfmsdkalmfsadikfjisaodjfosadjfmsadkmfsdnmfiosndafoinsdaiofnsdaf'    # 79 >> f

print(solution(s1))


# print(len(s1))
# print(len(s1)//2)
