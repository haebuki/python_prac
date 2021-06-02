#
#  topic : 이진 탐색
'''
 description : sw expert academy list2 problem
 reference!
'''
#  @author haebuki
#  @date 2021-05-28
#  @version None 작업 내용 None
#  @see None

test_case = int(input())

for tc in range(1,test_case+1):
    result = 0
    search = 0
    P,Pa,Pb = map(int,input().split(" "))
    start = [1, 1]
    end = [P, P]
    while 1:
        search = [int((start[0]+end[0])/2),int((start[1]+end[1])/2)]

        if search[0] == Pa and search[1] == Pb:
            result = '0'
            break
        elif search[0] == Pa:
            result = 'A'
            break
        elif search[1] == Pb:
            result = 'B'
            break

        if Pa > search[0]:
            start[0] = search[0]
        elif Pa < search[0]:
            end[0] = search[0]
        if Pb > search[1]:
            start[1] = search[1]
        elif Pb < search[1]:
            end[1] = search[1]

    print("#{} {}".format(tc,result))
