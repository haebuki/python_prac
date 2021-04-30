def rsp(mine,your):
    allowed = ['가우','바우']
    if mine not in allowed or your not in allowed:
        raise ValueError

try:
    rsp('가위','바우')
except:
    print("잘못넣음")


school = {'1반': [172,185,198,177,165,199], '2반':[165,177,167,180,191]}

try:
    for class_number, students in school.items():
        for student in students:
            if student > 190:
                print(class_number,'반에 190을 넘는 학생이 있습니다.')
                raise StopIteration
except:
    print('정상종료')