# 관호변환

# u = 균형잡힌 문자열 >> '('의 개수와 ')' 개수가 같아지는 지점까지


# u와 v를 나눠주는 함수
def divide(p):
    cnt_l = 0
    cnt_r = 0

    for i in range(len(p)):
        if p[i] == '(':
            cnt_l += 1
        else:
            cnt_r += 1

        if cnt_l == cnt_r:
            break

    return p[:i+1], p[i+1:]


def check_str(s):
    result = True
    cnt = 0

    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            result = False
            break

    return result


def solution(p):
    if p is '':
        return ''

    u, v = divide(p)
    if check_str(u) == True:

        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        # u의 첫 번째, 마지막 제거
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('

    return answer


###################################################
p = "(()())()"
# p = "()))((()"
print(solution(p), end='\n\n')
###################################################
