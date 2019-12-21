# 캐시

## LRU : 가장 오래된 것부터 제거


def solution(cacheSize, cities):
    cache = []
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    for c in cities:
        c = c.lower()

        if c in cache: # 리스트에 있다면 패스
            cache.pop(cache.index(c))
            cache.append(c)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(c)
            else:
                cache = cache[1:] + [c]
            
            answer += 5

    return answer



################################################################################
cacheSize = 2
# cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
# cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

print(solution(cacheSize, cities))
################################################################################
