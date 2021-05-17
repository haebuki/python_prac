#sw academy min,max solution

T = int(input())

for count in range(0,T):
    input()
    a = list(map(int,input().split()))
    print("#{} {}".format(count+1,max(a)-min(a)))