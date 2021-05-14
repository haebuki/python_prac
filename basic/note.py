import collections

my_list = [1,2,3,4,5,6,7,8,7,9,1,2,3,3,44,2,6,4,3,6,3]
answer = collections.Counter(my_list)

print(type(answer))