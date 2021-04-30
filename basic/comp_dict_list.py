list = [1,2,3,4,5]
list1= [1,2,3]
dict = {'a':1,'b':2}
dict1 = {'a':5, 'c': 3, 'b': 2}

list2 = list + list1

print(list2)


dict1.update(dict)
print(dict1)

print(dict1.keys())


print(2 in dict.values())

dict.clear()

print(dict)

#수정