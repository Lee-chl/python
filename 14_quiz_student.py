class Student:
    def __init__(self,grade,cl,name):
        self.grade = grade
        self.cl = cl
        self.name = name
    def intro(self):
        print('{}학년 {}반 {}입니다.'.format(self.grade,self.cl,self.name))

student1 = Student(1,3,'hoho');
student1.intro()

student2 = Student(3,2,'hihi');
student2.intro()