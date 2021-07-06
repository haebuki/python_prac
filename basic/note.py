#
#  topic : 미로
#  description : SW expert academy [string 학습] 문제 풀이
#
#  @author haebuki
#  @date 2021-07-06
#  @version None 작업 내용 None
#  @see None
#
dx=[1,0,-1,0]
dy=[0,1,0,-1]

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    map1=[]
    stack1=[]
    result=0

    for _ in range(N):
        map1.append(list(map(int,input())))

    for index,value in enumerate(map1):
        try:
            init_x=index
            init_y=value.index(3)
            stack1.append([init_x,init_y])
        except:
            pass

    while 1:
        temp=stack1.pop()

        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]

            if x > N-1 or x < 0 or y > N-1 or y < 0:
                continue
            if map1[x][y] == 2:
                result = 1
                break
            if map1[x][y] != 0:
                continue

            map1[x][y]=1
            stack1.append([x,y])

        if len(stack1)==0 or result==1:
            break
    print("#{} {}".format(tc, result))
