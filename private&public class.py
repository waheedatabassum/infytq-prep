
class Student:
    __college="Aditya"
    def __init__(self,rollno,name,fee):
        self.rollno=rollno
        self.name=name
        self.fee=fee
    def display(self):
        print(self __college)#private instant variable
        #so as to call private method
        def display(self):
            self.  __display()

            
s1=Student(123,"hira",2000)
#public instant variable
#print(s1.rollno,s1. __college)
s1.display()
