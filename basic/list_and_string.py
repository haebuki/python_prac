my_list = [1,2,3,4,5,6]

print(my_list[0])

str = "Hello world"

print(str[1])

print(3 in my_list)
print('H' in str)

print(my_list.index(5))

characters = list("abcdef")
print(characters)

words = "Hello world는 프로그래밍을 배우기에 아주 좋은 사이트 입니다."
world_list = words.split()

print(world_list)
time = "10:35:59"

time_list = time.split(':')

print(time_list)

join_list = ":".join(time_list)

print(join_list)