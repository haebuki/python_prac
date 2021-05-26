#
#  topic : 구간합
'''
 description : SW expert academy [List1 학습] 문제 풀이
 reference!
'''
#  @author haebuki
#  @date 2021-05-25
#  @version None 작업 내용 None
#  @see None

#정답
TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))

    lst = []
    for i in range(N-M+1):
        lst.append(sum(Data[i:i+M]))

    print('#%s %d'%(tc, max(lst)-min(lst)))

#  내 코드(runtime error 발생!).. 시간 요소를 줄여야한다.. api를 적극 활용하자..
''' 
test_case = input()

for testcase in range(0,int(test_case)):
    N, M = input().split(" ")

    case_list = list(input().split(" "))
    index=0
    count = 0
    max_result = 0
    min_result = 99999
    summ = 0
    while 1:
        summ += int(case_list[index])
        count += 1
        index += 1
        if count == int(M):
            if max_result < summ:
                max_result = summ
            if min_result > summ:
                min_result = summ
            if index == len(case_list):
                break
            summ -= int(case_list[index-int(M)])
            count -= 1

    print("#{} {}".format(testcase + 1, max_result-min_result))
'''
