from flask import Flask
import datetime
from random import *
import random

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hell World..'

@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'

@app.route('/dday')
def dday():
    today=datetime.datetime.now()
    endsaffy=datetime.datetime(2019, 11, 29)
    td=endsaffy - today
    return f'SSAFY 1학기 종료까지 {td.days}일 남았습니다.'
@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄로 작성해봅시다!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다 {name}님!'

@app.route('/cube/<int:number>')
def mul(number):
    return f'{number}의 3제곱은 {number**3}입니다.'


# 점심 메뉴 리스트(5개)에서 2개를 뽑아 출력하기
@app.route('/lunch/<int:person>')
def lunch(person):
    menu=['김밥','석쇠','부리또','짜장면','햄버거']
    return f'{random.sample(menu, person)}'



