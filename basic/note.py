#
#  topic : 숫자카드
#  description : SW expert academy [List1 학습] 문제 풀이
#
#  @author haebuki
#  @date 2021-05-25
#  @version None 작업 내용 None
#  @see None
#
#  reference! 시간적 요소 때문에 fail이 떴음,
#  for문에서 0~9를 검사하지 않아도 card에 있는 수만 검사하면 되므로
#  card의 iteration만 검사하자
test_case = int(input())

for testcase in range(0,test_case):
    input()

    card = list(map(int,input()))
    max_result = 0
    result = 0
    for i in card:
        if max_result < card.count(i):
            max_result = card.count(i)
            result = i
    if max_result == 1:
        result = max(card)

    print("#{} {} {}".format(testcase + 1, result, max_result))





