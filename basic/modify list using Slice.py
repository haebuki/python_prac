numbers = list(range(10))

print(numbers)

del numbers[0]

print (numbers)

del numbers[:5]

print (numbers)

print(numbers[1:3])

numbers[1:3]=[33,22,66]

print (numbers)

numbers[1:3] = [1]

print (numbers)