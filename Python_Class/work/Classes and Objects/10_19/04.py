# 4.学生有姓名(name)和成绩(score)信息。成绩有科目(course)和分数(grade)信息。学生类的getResult方法显
# 示输出成绩信息，setData方法实现初始化学生信息。编写学生类(Student)和成绩类(Score)，并调用这些方法
class Score:
    def __init__(self,course,grade):
        self.course = course
        self.grade = grade
class Student(Score):
    def __init__(self,name,score):
        self.name = name
        self,score = score

