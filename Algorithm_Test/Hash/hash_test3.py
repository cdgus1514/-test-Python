from collections import Counter

def solution(clothes):
    clothes_category = Counter([cat for _, cat in clothes])
    print(type(clothes_category))
    all_possible = 1

    for key in clothes_category:
        all_possible *= clothes_category[key] + 1

    
    return all_possible-1




######################################################################################################

# clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

######################################################################################################

print(solution(clothes))


########### summary ###########

# Counter >> 집합에서 각 원소의 출현 횟수를 세어서 유지
