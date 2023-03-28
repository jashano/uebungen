class Student:
    def __init__(self, name, vorname):
        self.name=name
        self.vorname=vorname

class Programmierkurs:
    def __init__(self,name):
        self.name = name
        self.students=[]

    def addStudent(self, stud):
        self.students.append(stud)

kurs = Programmierkurs("Geoprogrammierung1")
stud1 = Student("Müller","Hans")
stud2 = Student("Meier","Anna")

kurs.addStudent(stud1)
kurs.addStudent(stud2)