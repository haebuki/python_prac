#
#  topic : 종이붙이기
#  description : SW expert academy [string 학습] 문제 풀이
#
#  @author haebuki
#  @date 2021-06-25
#  @version None 작업 내용 None
#  @see None
#
f = [0 for _ in range(100)]
test_case = int(input())

for tc in range(1,test_case+1):
    result=0
    f[0]=1
    f[1]=3
    N = int(int(input())/10)

    for n in range(2,N+1):
        if f[n]==0:
            f[n]=(2*f[n-2]+f[n-1])


    print("#{} {}".format(tc, f[N-1]))