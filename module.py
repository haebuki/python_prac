import math
import random

a = ['가위', '바위', '보']

selected = random.choice(a)

print(selected)


def get_web(url):
    """URL을 넣으면 페이지 내용을 올려주는 함수"""
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹페이지 주소? ')
content = get_web(url)
print(content)