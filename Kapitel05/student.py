class Student:
    def __init__(self,name,vorname,geschlecht,matrnr,age=0):
        self.name=name
        self.vorname=vorname
        self.geschlecht=geschlecht
        self.matrnr=matrnr
        self.setAge(age)
        self.mark={}
    
    def setAge(self,age):
        self.age=age
    
    def setMark(self,topic,mark):
        self.mark[topic]=mark

    def display(self):
        return f"({self.name},{self.vorname},{self.geschlecht},{self.matrnr},{self.age},{self.mark})"
    

a=Student('Meier','Hans','m',10738797)
print(a.display())
a.setAge(12)
print(a.display())
a.setMark('Geoprogrammierung',5)
print(a.display())
