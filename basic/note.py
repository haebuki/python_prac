#
#  topic : parenthesis search 
#  description : SW expert academy [string 학습] 문제 풀이
#
#  @author haebuki
#  @date 2021-06-8
#  @version None 작업 내용 None
#  @see None
#
test_case = int(input())

for tc in range(1,test_case+1):
	str = input()
	result = 1
	stack1=[]
	for i in str:
			if i == '(' or i=='{':
				stack1.append(i)
			elif i==')' or i=='}':
				if stack1:
					a=stack1.pop()	
				else:
					result=0
					break	
				if i==')' and a=='{':
					result=0
					break
				if i=='}' and a=='(':
					result=0
					break
					
	if len(stack1)!=0:
		result=0
	
	print("#{} {}".format(tc,result))
	
