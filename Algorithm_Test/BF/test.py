def solution(array, commands):
    
    answer = []

    for i in range(len(commands)):
        cutarry = array[int(commands[i][0]-1):int(commands[i][1])]
        cutarry.sort()
        answer.append(cutarry[int(commands[i][2]-1)])
    
    return answer
















###################################################################
array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]

# 1) [2,5,3] >> [5,2,6,3]       >> [2,3,5,6]       >> [5]
# 2) [4,4,1] >> [6]             >> [6]             >> [6]
# 3) [1,7,3] >> [1,5,2,6,3,7,4] >> [1,2,3,4,5,6,7] >> [3]
###################################################################



print(solution(array, commands))

# print(commands[0][0])
# print(commands[0][1])
# print(commands[0][2])


# test = array[1:5]
# print(test)
# test.sort()
# print(test)

# print(test[3-1])