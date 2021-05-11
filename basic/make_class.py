class Human():
    '''사람'''

person1 = Human()
person2 = Human()
person1.language = '한국어'
person2.language = 'English'

print(person1.language)
print(person2.language)

person1.name = '서울시민'
person2.name = '미국인'

print(person1.name)
print(person2.name)

def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name, person.language))

Human.speak = speak

person1.speak()
person2.speak()