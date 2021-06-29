#
#  topic : 그래프 경로
#  description : SW expert academy [string 학습] 문제 풀이
#
#  @author haebuki
#  @date 2021-06-29
#  @version None 작업 내용 None
#  @see None
#
test_case = int(input())

for tc in range(1,test_case+1):
    result=0
    stack1=[]
    V,E = map(int, input().split())
    map1 = [[0 for _ in range(V)] for _ in range(V)]

    for _ in range(E):
        X,Y = map(int, input().split())
        map1[X-1][Y-1] = 1
    S, G = map(int, input().split())
    S -=1
    G -=1
    stack1.append(S)

    while 1:
        a = stack1.pop()
        for i in range(V):
            #stack1에서 경로를 꺼내고 모든 노드의
            #방향을 검사하고 이어져있는 경로를 스택에 저장
            #찾고자하는 Y까지의 경로가 1이면 1 출력
            if map1[a][G]==1:
                result=1
                break
            if map1[a][i] == 1:
                stack1.append(i)
                continue

        if len(stack1)==0 or result==1:
            break

    print("#{} {}".format(tc, result))