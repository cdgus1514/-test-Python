def solution(s):
    min_len = len(s)

    for length in range(1, len(s)//2+1):
        cnt = 1
        result = ""
        previous = s[:length]
        check_len = length

        while check_len <= len(s):
            now = s[check_len: check_len + length]
            check_len += length
            if previous == now:
                cnt += 1

            else:
                if cnt == 1 : result += previous
                else : result += str(cnt) + previous
                cnt = 1
                previous = now
        
        if cnt == 1 : result += previous
        else : result += str(cnt) + previous
        
        if min_len > len(result) : min_len = len(result)

    return min_len



# s1 = 'aaaaaaaaaa'
# s1 = 'xababcdcdababcdcd'
# s1 = 'aabbaccc'
# s1 = 'abcabcabcabcdededededede'
s1 = 'abcababcabcabcabcdedededededeabcabcabcabcxababcdcdababcdcdxababcdcdabxababcdcdababcdcdabcdcdxababcdcdababcdcdxababcdcdababcdcxababcdcdababcdcdddedededededecabcaabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabxababcdcdababcdcdcabcabcabcdedededededeabcxababcdcdababcdcdabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededeabcabcabcabcdedededededexababcdcdababcdcdbcdexababcdcdababcdcddedededede'
print(solution(s1))