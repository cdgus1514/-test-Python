import pandas as pd

dates = ['', '오늘', '내일', '이번주', '다음주']

locations = ['서울', '인천', '부산', '대구', '광주', '울산', '대전', '광명', '파주', '창원', '평택',
             '제주도', '전주', '용인', '수원', '청주', '안산', '시흥', '춘천', '목포', '경주', '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '미지정', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구',
             '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '연제구', '수영구', '사상구', '기장군',
             '미추홀구', '연수구', '남동구', '부평구', '계양구', '수성구', '달서구', '홍대', '건대', '신촌', '이태원', '강남역', '신논현역', '가로수길', '인사동']

end1 = ['어때', '어떠니', '알려줘', '알려주세요']
end2 = ['맑니', '맑을까', '덥니', '더울까', '춥니', '추울까',
        '흐리니', '흐릴까', '비오니', '비올까', '눈오니', '눈올까']
end3 = ['필요해', '필요하니', '필요할까', '챙길까', '쓸까']


def makeExel1(items, col, path):
    result = []

    for item in items:
        result.append([item] + [col])

    data = pd.DataFrame(result, columns=('question', 'intent'))
    data.to_csv(path, encoding='cp949', mode='a', index=False, header=True)


def makeExel2(items, col, path):
    result = []

    for item in items:
        result.append([item] + [col])

    data = pd.DataFrame(result, columns=('question', 'intent'))
    data.to_csv(path, encoding='cp949', mode='a', index=False, header=False)

################################################ 날씨 ################################################
# 지역 날씨 어때/어떠니/알려줘/알려주세요
# 오늘 지역 날씨 어때/어떠니/알려줘/알려주세요
# 내일 지역 날씨 어때/어떠니/알려줘/알려주세요
# 이번주 지역 날씨 어때/어떠니/알려줘/알려주세요
# 다음주 지역 날씨 어때/어떠니/알려줘/알려주세요

# 지역 맑니/맑을까/덥니/더울까/춥니/추울까/흐리니/흐릴까/비오니/비올까/눈오니/눈올까
# 오늘 지역 맑니/맑을까/덥니/더울까/춥니/추울까/흐리니/흐릴까/비오니/비올까/눈오니/눈올까
# 내일 지역 맑니/맑을까/덥니/더울까/춥니/추울까/흐리니/흐릴까/비오니/비올까/눈오니/눈올까
# 이번주 지역 맑니/맑을까/덥니/더울까/춥니/추울까/흐리니/흐릴까/비오니/비올까/눈오니/눈올까
# 다음주 지역 맑니/맑을까/덥니/더울까/춥니/추울까/흐리니/흐릴까/비오니/비올까/눈오니/눈올까


# 지역 우산 필요해/필요하니/필요할까/챙길까
# 오늘 지역 우산 필요해/필요하니/필요할까/챙길까
# 내일 지역 우산 필요해/필요하니/필요할까/챙길까
# 이번주 지역 우산 필요해/필요하니/필요할까/챙길까
# 다음주 지역 우산 필요해/필요하니/필요할까/챙길까
#####################################################################################################
dusts = ['먼지', '먼지 상태', '미세먼지', '미세먼지 상태', '공기', '공기 상태', '먼지 수치', '미세먼지 수치']
################################################ 먼지 ################################################
# 지역 먼지/미세먼지/공기/먼지수치/미세먼지 수치/ 어때/어떠니/알려줘/알려주세요
# 오늘 지역 먼지/미세먼지/공기/먼지수치/미세먼지 수치/ 어때/어떠니/알려줘/알려주세요
# 내일 지역 먼지/미세먼지/공기/먼지수치/미세먼지 수치/ 어때/어떠니/알려줘/알려주세요
# 이번주 지역 먼지/미세먼지/공기/먼지수치/미세먼지 수치/ 어때/어떠니/알려줘/알려주세요
# 다음주 지역 먼지/미세먼지/공기/먼지수치/미세먼지 수치/ 어때/어떠니/알려줘/알려주세요

# 지역 마스크 필요해/필요하니/필요할까/챙길까
# 오늘 지역 마스크 필요해/필요하니/필요할까/챙길까
# 내일 지역 마스크 필요해/필요하니/필요할까/챙길까
# 이번주 지역 마스크 필요해/필요하니/필요할까/챙길까
# 다음주 지역 마스크 필요해/필요하니/필요할까/챙길까
#####################################################################################################
foods = ['햄버거', '수제버거', '치킨', '통닭', '양념치킨', '스테이크', '파스타', '라면', '부대찌개', '한식', '양식', '중식', '일식', '분식', '백반', '감자탕', '아구찜', '매운탕', '마라롱샤', '마라탕', '만두', '찜닭', '브런치', '카레', '케익', '연어초밥', '고기국수',
         '피자', '순대', '갈비', '회', '족발', '떡볶이', '순대', '국수', '스파게티', '크림파스타', '돈까스', '티본스테이크', '소고기', '바베큐', '태국음식', '베트남음식', '멕시코음식', '인도음식', '마카롱', '돼지국밥', '밀면', '쌀국수', '곱창', '막창', '양대창']
stores = ['카페', '와인바', '바', '브런치카페', '페밀리레스토랑', '라운지바', '칵테일바', '맥주바']
ad1 = ['', '근처', '주변', '인기많은', '유명한']
ad2 = ['', '근처', '주변', '인기많은', '유명한', '분위기 좋은']
end4 = ['알려줘', '알려주세요', '추천해줘']
################################################ 맛집 ################################################

cnt = []

weather = []
for date in dates:
    for location in locations:
        for i in end1:
            if date == '':
                weather.append(location+' '+'날씨'+' '+i)
            else:
                weather.append(date+' '+location+' '+'날씨'+' '+i)

for date in dates:
    for location in locations:
        for i in end2:
            if date == '':
                weather.append(location+' '+i)
            else:
                weather.append(date+' '+location+' '+i)

for date in dates:
    for location in locations:
        for i in end3:
            if date == '':
                weather.append(location+' '+'우산'+' '+i)
            else:
                weather.append(date+' '+location+' '+'우산'+' '+i)


dust = []
for date in dates:
    for location in locations:
        for d in dusts:
            for i in end1:
                if date == '':
                    dust.append(location+' '+d+' '+i)
                else:
                    dust.append(date+' '+location+' '+d+' '+i)


for date in dates:
    for location in locations:
        for i in end3:
            if date == '':
                dust.append(location+' '+'마스크'+' '+i)
            else:
                dust.append(date+' '+location+' '+'마스크'+' '+i)


restaurant = []
for location in locations:
    for food in foods:
        for ad in ad1:
            for i in end4:
                if ad == '':
                    restaurant.append(location+' '+food+' '+'맛집'+' '+i)
                else:
                    restaurant.append(location+' '+ad+' '+food+' '+'맛집'+' '+i)

for location in locations:
    for store in stores:
        for ad in ad2:
            for i in end4:
                if ad == '':
                    restaurant.append(location+' '+store+' '+i)
                else:
                    restaurant.append(location+' '+ad+' '+store+' '+i)


################################################ 저장 ################################################
print('날씨 훈련데이터셋 개수 >> ', len(weather))
cnt.append(int(len(weather)))
makeExel1(weather, '날씨', 'intent_dataset.csv')

print('미세먼지 훈련데이터셋 개수 >> ', len(dust))
cnt.append(int(len(dust)))
makeExel2(dust, '먼지', 'intent_dataset.csv')

print('맛집 훈련데이터셋 개수 >> ', len(restaurant))
cnt.append(int(len(restaurant)))
makeExel2(restaurant, '맛집', 'intent_dataset.csv')

total = sum(cnt)
print('최총 Intent 훈련데이터셋 개수 >> ', total)