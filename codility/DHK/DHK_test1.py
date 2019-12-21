# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import permutations


def solution(A, B, C, D):
    date = [A, B, C, D]
    time = []
    test = list(permutations(date, 4))

    for i in test:
        h = str(i[0]) + str(i[1])
        if int(h) <= 23:
            m = str(i[2]) + str(i[3])
            if int(m) <= 59 and int(h) == 23:
                time.append(h + ":" + m)
            elif int(m) <= 60 and int(h) != 23:
                time.append(h + ':' + m)

    result = set(time)

    return len(result)

pr