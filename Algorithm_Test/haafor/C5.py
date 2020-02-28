# 라이브러리 사용하지 않고 중앙값 찾기

test = [4, 3, 1, 2, 6, 7, 10]
test.sort()

if len(test) % 2 == 0:
    median1 = test[len(test)//2]
    median2 = test[len(test)//2 -1]
    median = (median1 + median2)/2
else:
    median = test[len(test)//2]

print('중앙값 >> ', median)


##########################################################
# import statistics
#
# solve = statistics.median(test)
# print(solve)