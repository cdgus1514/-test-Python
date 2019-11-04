from collections import Counter

def solution(clothes):
    clothes_category = Counter([cat for _, cat in clothes])
    all_possible = 1

    for key in clothes_category:
        all_possible *= clothes_category[key] + 1

    
    return all_possible-1




######################################################################################################

# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

######################################################################################################

# print(solution(clothes))


clothes_category = Counter([cat for _, cat in clothes])
all_possible = 1

for key in clothes_category:
    all_possible *= clothes_category[key] + 1

print(all_possible-1)



clothes_category = dict()
###########

for i in clothes:

    if clothes[i][0] in clothes_category:
        clothes_category[clothes[i][1]] = list.append(clothes[i][0])
    else:
        clothes_category[clothes[i][1]] = list(clothes[i][0])