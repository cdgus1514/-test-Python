board = [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]


'''
def check_object(m, board):
    tmp = 0

    for i in range(5):
        if board[i][m-1] == 0:
            continue
        else:
            tmp = board[i][m-1]
            board[i][m-1] = 0
            break
    
    return tmp


def solution(board, moves):
    box = []
    cnt = 0

    for i in moves:
        a =  check_object(i, board)
        if a == 0:
            continue
        else:
            box.append(a)
        
    print(box, end="\n\n")


    while True:
        for i in range(len(box)):
            if i < len(box)-1:
                if box[i] == box[i+1]:
                    del box[i+1]
                    cnt += 1
                    del box[i]
                    cnt += 1
                    break
                
                print(box)

            else:
                return cnt
'''

# box = []
# cnt = 0
# while True:
#     for i in moves:
#         a =  check_object(i)
#         if a == 0:
#             continue
#         else:
#             box.append(a)
        
#         print(box, end="\n\n")
    
#     for i in range(len(box)):
#         if i < len(box)-1:
#             if box[i] == box[i+1]:
#                 del box[i+1]
#                 cnt += 1
#                 del box[i]
#                 cnt += 1
        
#         else:
#             return cnt


def check_object(m, board):
    tmp = 0

    for i in range(5):
        if board[i][m-1] == 0:
            continue
        else:
            tmp = board[i][m-1]
            board[i][m-1] = 0
            break
    
    return tmp


def solution(board, moves):
    box = []
    cnt = 0

    for i in moves:
        a =  check_object(i, board) 
        if a == 0:
            continue
        else:
            box.append(a)
        
        try:
            for i in range(len(box)):
                if box[i] == box[i+1] and i !=len(box):
                    del box[i+1]
                    cnt += 1
                    del box[i]
                    cnt += 1
                    continue
                
            if i == len(box):
                return cnt

        except:
            pass



print(solution(board, moves))