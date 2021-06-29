#
#  topic : 반복문자 지우기
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
    str = list(input())
    stack1 = []

    for i in str:
        if len(stack1) == 0:
            pass
        elif stack1[-1] == i:
            stack1.pop()
            continue

        stack1.append(i)

    result = len(stack1)

    print("#{} {}".format(tc, result))