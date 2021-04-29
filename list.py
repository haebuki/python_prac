list2 = [1,2,3,4,5,6]
print('list2={}'.format(list2))

list2.append(3) # 리스트 뒤에 추가
print(list2)

list3 = list2 + [13]#새로운 리스트를 생성

print(list3)

list4 = list2 + list3

print(list4)

n=12

ownership = n in list3
print(ownership)

n=4
if n in list2:
    print('{}은 있어!'.format(n))

print(list3)
del(list3[3])
print(list3)

list3.remove(1)
print(list3)