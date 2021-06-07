#
#  topic : 특별한 정렬
'''
 description : sw expert academy list2 problem
 reference! split 함수는 split(" ")와 split()의 의미는 같지만 실행속도에 대한 차이가 있따.
 아무래도 모든 요소를 반복하며 스페이스를 찾고 나누는 작업이 있기때문에 훨씬 느린게 아닐까 싶다..
 저거떄문에 너무 많은 런타임 에러를 겪엇다... ㅠㅠ 앞으로는 자동으로 스플릿될 수 있는 상황이면 split()원형을 쓰자..
'''
#  @author haebuki
#  @date 2021-05-28
#  @version None 작업 내용 None
#  @see None

testcase = int(input())

for tc in range(1, testcase + 1):
    N = input()
    aj = list(map(int, input().split()))
    sorted_list = []
    aj.sort()
    for i in range(0,10):
        if i % 2 == 0 :
            sorted_list.append(aj.pop())
        else:
            sorted_list.append(aj.pop(0))
    print("#{} ".format(tc), end="")
    print(*sorted_list)