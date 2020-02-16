

class Student:

    
    school = 'xyz'
    
    def __init__(self,eng,m1):
        self.eng = eng
        self.m1 = m1
        
    def avg(self):
        return (self.eng + self.m1)/2
    #getters(accessors)
    def get_m1(self):
        return self.m1
    #setters(mutators)
    def set_m1(self,value):
        self.m1 = value


        
s1 = Student(21,34)
s2 = Student(19,41)


print(s2.avg())

        
