## k번째 수

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        cutarray = array[commands[i][0]-1:commands[i][1]]
        cutarray.sort()
        answer.append(cutarray[commands[i][2]-1])
    
    return answer







###################################################
array = [1,5,2,6,3,7,4]
command = [[2,5,3], [4,4,1], [1,7,3]]

print(solution(array, command))