a = [0 for i in range(400)]

my_str = input().strip()

for element in my_str:
    a[ord(element)]+=1

max = 0
result=[]

for index,element in enumerate(a):
    if element > max:
        result.clear()
        max = element
        result+=[index]
    elif element == max:
        result+=[index]

print("".join(map(chr,result)))