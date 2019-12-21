def solution(s):
    mini = len(s)
    print(mini, end="\n\n")

    for length in range(1, len(s)//2+1) :
        cnt = 1
        result = ''
        previous = s[:length]
        # print('previous >> ', previous)
        total_length = length
        # print('total_length >> ', total_length)

        while total_length <= len(s) :
            now = s[total_length: total_length + length]
            # print('now >> ', now)
            total_length += length
            if previous == now :
                cnt += 1

            else :
                if cnt == 1 : result += previous
                else : result += str(cnt) + previous
                cnt = 1
                previous = now

        if cnt == 1 : result += previous
        else : result += str(cnt) + previous

        print('result >> ', result)
        if mini > len(result) : mini = len(result)
    
    return mini








# def solution(s):
#     min_len = len(s)

#     for length in range(1, len(s)//2+1):
#         cnt = 1
#         result = ""
#         previous = s[:length]
#         check_len = length

#         while check_len <= len(s):
#             now = s[check_len: check_len + length]
#             check_len += length
#             if previous == now:
#                 cnt += 1

#             else:
#                 if cnt == 1 : result += previous
#                 else : result += str(cnt) + previous
#                 cnt = 1
#                 previous = now
        
#         if cnt == 1 : result += previous
#         else : result += str(cnt) + previous
        
#         if min_len > len(result) : min_len = len(result)

#     return min_len


























s1 = 'aabbaccc'

print(solution(s1))