def solution(s):
    min_len = len(s)

    for length in range(1, len(s)//2+1):
        cnt = 1
        result = ""
        previous = s[:length]
        print('previous >> ', previous)
        check_len = length

        while check_len <= len(s):
            print('check_len ', check_len)
            now = s[check_len: check_len + length]
            print('now >> ', now)
            check_len += length

            if previous == now:
                cnt += 1
            else:
                if cnt == 1:
                    result += previous
                else:
                    result += str(cnt) + previous

                cnt = 1
                previous = now

        if cnt == 1:
            result += previous
        else:
            result += str(cnt) + previous

        print(result, end='\n\n')
        if min_len > len(result):
            min_len = len(result)

    return min_len


# s1 = 'aaaaaaaaaa'
# s1 = 'xababcdcdababcdcd'
s1 = 'aabbaccc'
# s1 = 'abcabcabcabcdededededede'
# s1 = 'abcababcabcabcabcdedededededeabcabcabcabcxababcdcdababcdcdxababcdcdabxababcdcdababcdcdabcdcdxababcdcdababcdcdxababcdcdababcdcxababcdcdababcdcdddedededededecabcaabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabxababcdcdababcdcdcabcabcabcdedededededeabcxababcdcdababcdcdabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededexababcdcdababcdcdbcdexababcdcdababcdcddedededede'
print(solution(s1))
