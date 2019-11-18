## 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    length = len(phone_book[0])
    end = len(phone_book)

    for i in range(1, end):
        check = map(''.join, zip(*[iter(phone_book[i])]*length))
        # print(type(check))    # <class 'map'>
        
        if phone_book[0] in check:
            return False
            
    return True


#################################################################
# phone_book = ['119', '97674223', '1195524421']
phone_book = 	["12", "123", "1235", "567", "88"]

print(solution(phone_book))
#################################################################



# zip, iterator 함수를 사용해서 원하는 개수만큼 문자열 자르기 반복
# map 함수로 새로운 리스트 생성