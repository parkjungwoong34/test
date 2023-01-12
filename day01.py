student = '김도훈'
subject = '오래된 미래'
print(student, '학생의 ', subject, '과목 성적은', subjects[subject], '입니다')
# old style
print("%s 학생의 %s 과목 성적은 %s 입니다"%(student, subject, subjects[subject]))
# modern style (format함수)
print("{0} 학생의 {1} 과목 성적은 {2}입니다".format(student, subject, subjects[subject]))
# ultra modern style
print (f'{student} 학생의 {subject} 과목 성적은 {subjects[subject]}입니다')
#f스트링
print(f'{student} 학생의 {subject} 과목 성적은 {subjects[subject]}입니다')

