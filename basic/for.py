"""patterns = [1,2,3,4,5,6,7,8,9,10]

for a in patterns:
    print(a)

for pattern in range(5):
    print(pattern)

names = ['철수', '영희', '바둑이', '귀도','해북이']

for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i+1, name))
print()
for i, name in enumerate(names):
    print('{}번 : {}'.format(i+1,name))

print(names)
"""
# now start repeat dictionary code

ages = {'tod':35, 'jane':23,'paul':62}

for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)

for key in ages:
    print(key)

for key, value in ages.items():
    print(key,value)

#수저