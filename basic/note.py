#
#  topic : 색칠하기
'''
 description : sw expert academy list2 problem
 reference!
'''
#  @author haebuki
#  @date 2021-05-27
#  @version None 작업 내용 None
#  @see None



test_case = int(input())

for tc in range(1,test_case+1):
    coord = [[0] * 10 for _ in range(0, 10)]

    N = int(input())

    clr = [[0]*5 for _ in range(N)]
    count=0
    for i in range(N):
        clr[i] = list(map(int, input().split(" ")))
        for j in range(clr[i][0],clr[i][2]+1):
            for k in range(clr[i][1],clr[i][3]+1):
                if clr[i][4] % 2 == 0:
                    coord[j][k] += 2
                else:
                    coord[j][k] += 1
    for i in range(10):
        if coord[i].count(3)!=0:
            count+=coord[i].count(3)
    print("#{} {}".format(tc,count))