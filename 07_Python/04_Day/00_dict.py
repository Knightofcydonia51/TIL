#1. 딕셔너리 만들기
lunch = {
    '중국집' : '02'
}

lunch = dict(중국집='02')
# print(lunch)

#2. 딕셔너리 내용 추가하기
lunch['분식집'] = '031'
# print(lunch)

# idol={
#     'Red velvet' : {
#         '슬기' : 26,
#         '예리' : 20
#     }
# }


#3. 딕셔너리 내용 출력
# print(idol['Red velvet']['슬기'])
# print(idol.get('Red velvet').get('슬기'))

#4. 딕셔너리 반복문 활용하기
# for key in lunch:
#     print(key)
#     print(lunch[key])

#4-2. .items() - key, value 모두 가져오기
# for key, value in lunch.items():
#     print(key, value)

#4-3. .values() - value만 가져오기
# for value in lunch.values():
#     print(value)

#4-4. .keys() - key만 가져오기
for key in lunch.keys():
    print(key)
