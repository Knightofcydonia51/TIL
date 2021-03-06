from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

api_url='https://api.telegram.org'
token= config('TELEGRAM_BOT_TOKEN')
chat_id=config('CHAT_ID')

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text=request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 구조 프린트 해보기
    from_telegram=request.get_json()
    # print(from_telegram)
    # if from_telegram.get('message') is not None:
    #     chat_id = from_telegram.get('message').get('from').get('id')
    #     print(chat_id)
    # return '', 200
    
    # 메세지 그대로 돌려보내기
    if from_telegram.get('message') is not None:
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
    #    print(res)

    # 번역해보기
        if text[0:4] == '/번역 ': #0번째부터 3번째까지 문자가 '/번역 '일시, 실행.
            headers = {'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
            data={'source': 'ko', 'target': 'en', 'text': text[4:]}

            papago_res=requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            print(papago_res.json())
            text = papago_res.json().get('message').get('result').get('translatedText')
            print(text)
        res=requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200