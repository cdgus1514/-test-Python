# def check_stone(i, jump, stones):
#     if stones[i] == 0:
#         jump += 1
#         flag = False
#     else:
#         flag = True

#     return jump, flag


# def solution(stones, k):
#     jump = 0
#     passCnt = 0

#     while True:
#         for i in range(len(stones)):
#             # jump, flag = check_stone(i, jump, stones)
#             if stones[i] == 0:
#                 jump += 1
#                 flag = False
#             else:
#                 flag = True
            

#             if jump == k:
#                 return ("최종 건너간 인원수 >> ", passCnt)

#             elif jump != 0 and jump != k and flag == False:
#                 print('jump >> ', jump)
#                 continue

#             stones[i] = stones[i] - 1
#             # stones[i] = tmp
#             print(stones)
#             jump = 0
        
#         passCnt += 1    
#         print('result list >>', stones, end="\n\n")
#         print('passCnt >>', passCnt)






def check_stone(i, jump, stones, k):
    
    for j in range(i, len(stones)):
        if stones[j] == 0:
            jump += 1
            flag = False
            
            if jump == k:
                break
        else:
            flag = True
        

    return jump, flag


def solution(stones, k):
    jump = 0
    passCnt = 0

    while True:
        for i in range(len(stones)):
            jump, flag = check_stone(i, jump, stones, k)
            
            if  jump == k:
                return passCnt
            
            elif jump != 0 and jump != k and flag == False:
                continue

            tmp = stones[i] - 1
            stones[i] = tmp
            jump = 0
        
        passCnt += 1












###################################################
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))
###################################################



'''
def solution(stones, k):
    jump = 0
    passCnt = 0

    while True:
        for i in range(len(stones)):
            if stones[i] == 0:
                jump += 1
                flag = False
            else:
                flag = True
            
            
            if jump == k:
                return passCnt

            elif jump != 0 and jump != k and flag == False:
                continue

            stones[i] = stones[i] - 1
            jump = 0
        
        passCnt += 1
'''