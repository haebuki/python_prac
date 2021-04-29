import random

wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}

messages = {
    'win' : '이겼다',
    'lose' : '졌다',
    'draw' : '비겼다'
}

def rsp (mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

print("컴퓨터와의 가위 바위 보 대결!")
yours = input('가우 바우 보 중 하나를 입력하세요 : ')

computer = random.choice(['가위', '바위', '보'])

result = rsp(computer, yours)
print('컴퓨터는 {}\n결과는 {}'.format(computer,messages[result]))