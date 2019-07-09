# 음계
# c d e f g a b C
# 1 2 3 4 5 6 7 8

#asd = [1,2,3,4,5,6,7,8]
#dsd = [8,7,6,5,4,3,2,1]

num = list(map(int, input(">> ").split()))
nums = ""

for i in range(len(num)):
    nums += str(num[i])

if nums == "12345678":
    print("Ascending")
elif nums == "87654321":
    print("Descending")
else:
    print("Mixed")
