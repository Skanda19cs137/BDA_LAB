from xml.dom import NamespaceErr


class Student:
    def __init__(self, name, rollno, m1,m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
    def accept(self, Name, Rollno , marks1, marks2):
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)
    def display(self, ob):
        print("Name   :", ob.name)
        print("Rollno :", ob.rollno)
        print("Marks1 :", ob.m1)
        print("Marks2 :", ob.m2)
        print("\n")
    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno ==rn):
                return i
    def delete(self , rn):
        i=obj.search(rn)
        del ls[i]
    def update(self, rn , No):
        i=obj.search(rn)
        roll= No
        ls[i].rollno=roll;

ls=[]
obj=Student('',0,0,0)
print("\n Opreations used,")
print("\n1.Accept student details \n2.Display student details \n3.Search the details of a student \n4.Delete details of a student\n5.Update details of a student \n6.Exit")

obj.accept("A",1,100,100)
obj.accept("B",2,90,90)
obj.accept("c",3,80,80)

print("\nlist of students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

print("Student found")
s=obj.search(2)
obj.display(ls[s])

obj.delete(2)
print(ls.__len__())
print("List after deletion:")
for i in range(ls.__len__()):
    obj.display(ls[i])

obj.update(3,2)
print(ls.__len__())
print("List after updation:")
for i in range(ls.__len__()):
    obj.display(ls[i])

