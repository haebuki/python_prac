#
#  topic : 글자수
#  description : SW expert academy [string 학습] 문제 풀이
#
#  @author haebuki
#  @date 2021-06-25
#  @version None 작업 내용 None
#  @see None
#
test_case = int(input())

for tc in range(1,test_case+1):
    str1 = list(input())
    str2 = input()

    max = 0

    for i in str1:
        if str2.count(i) > max:
            max = str2.count(i)

    print("#{} {}".format(tc, max))
