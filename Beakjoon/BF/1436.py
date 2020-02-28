# 영화감독 숌

# N = int(input())
#
# 666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668
# 6669, 7666 ...

# 666부터 +1씩 BF >> 666패턴이 있으면 input-1
# print(str(N-1)+'666')


N = int(input())
name = 666

while N:
    if "666" in str(name):
        N -= 1
        print("N={}, name={}".format(N, name))

    name += 1

print(name - 1)