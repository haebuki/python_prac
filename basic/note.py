test_case = int(input())

for tc in range(1,test_case+1):
    N, M = map(int, input().split())
    map1=[]
    map2=[]
    end_flag=0
    result=[]

    #create map and reversed map
    for i in range(N):
        map1.append(list(input()))
    map2=list(zip(*map1))

    for i in range(N):
        index=0
        while True:
            if map1[i][index:index+M] == list(reversed(map1[i][index:index+M])):
                result = map1[i][index:index+M]
                end_flag = 1
                break
            elif map2[i][index:index+M] == tuple(reversed(map2[i][index:index+M])):
                result = map2[i][index:index + M]
                end_flag = 1
                break
            else:
                index+=1

            if index+M > N:
                break
    if end_flag==1:
        print("#{} {}".format(tc,"".join(result)))


