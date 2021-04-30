list1=[1,2,3,4,5]

try:
    print(list1.index(7))
except:
    print('잘못된 인덱스입니다.')

list1.append(22)

print(list1)
list1.extend([30,40,50])
print(list1)
list1.insert(1,20)
print(list1)
list2 = [30]
list1=list1+list2
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
