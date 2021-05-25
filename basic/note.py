#
#  program : 전기버스
#  description : SW expert academy [List1 학습] 문제 풀이
#
#  @author haebuki
#  @date 2021-05-25
#  @version None 작업 내용 None
#  @see None
#
test_case = input()

for testcase in range(0,int(test_case)):
    flag=0
    K,N,M = input().split()
    station_num = list(map(int,input().split()))
    station_num.append(int(N))

    #만약 정류장 사이 간격이 최대 거리량보다 크면 0 반환
    for index in range(0,len(station_num)-1):
        if int(K) < (station_num[index+1] - station_num[index]):
            print("#{} {}".format(testcase + 1, '0'))
            flag = 1

    if flag == 1 :
        continue

    # 정류장 사이 간격이 최대 거리량보다 작으면,
    # 최소 충전 횟수를 반환

    loc = 0
    charge = int(K)
    result = 0
    #4 7 9 14 17
    while 1:
        if loc == station_num[-1]:
            break
        if index > len(station_num)-1:
            continue
        if (station_num[index] - loc) > charge:
            index-=1
            loc = station_num[index]
            result+=1
            break
        else:
            index+=1
    print("#{} {}".format(testcase + 1, result))






