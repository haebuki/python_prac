class Human():
    '''닝겐'''
    def __init__(self,name,weight):
        print("__init__실행")
        self.name = name
        self.weight = weight
        print("이름은 {}, 몸무게는 {}".format(name,weight))

    def __str__(self):
        print()

    def create_human(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg가 되었습니다.".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg가 되었습니다.".format(self.name, self.weight))


# person = Human.create_human("철수",60.5)
person = Human("영희", 45)

person.walk()
person.eat()
person.walk()




