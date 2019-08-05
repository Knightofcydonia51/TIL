def my_url(itemPerPage=10, **args):
   if itemPerPage not in range(1,11):
       return ('1~10까지의 값을 넣어주세요.')
   if 'key' not in args or args.get('targetDt') == '':
       return('필수 요청변수가 누락되었습니다')
   base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
   base_url += f'itemPerPage={itemPerPage}'
   print(base_url)
   for key, value in args.items():
       base_url += f'{key}={value}&'
       print(base_url)
   return base_url