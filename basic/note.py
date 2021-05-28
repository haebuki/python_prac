#
#  topic : 부분집합의 합
'''
 description : sw expert academy list2 problem
 reference!
'''
#  @author haebuki
#  @date 2021-05-28
#  @version None 작업 내용 None
#  @see None

A = [i for i in range(1,13)]

test_case = int(input())

for tc in range(1,test_case+1):
    count = 0

    N,K = map(int,input().split(" "))

    for i in range(1<<len(A)):
        temp=[]
        for j in range(len(A)):
            if i & (1<<j):
                temp.append(A[j])
        if len(temp)== N and sum(temp)==K:
            count+=1
    print("#{} {}".format(tc,count))