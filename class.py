from abc import ABC,abstractmethod
class Student(ABC):
    def __init__(self,rollno,name,fee):
        self.rollno=rollno
        self.name=name
        self.fee=fee
        @abstractmethod
        def sspro(self):
            pass
        @abstractmethod
        def inpro(self):
            pass
class Hosteler(Student):
    def __init__(self,roomno,hfee):
        self.roomno=roomno
        self.hfee=hfee
        pass
class DS(Student):
    def __init__(self,busno,bfee):
        self.busno=busno
        self.bfee=bfee
H1=Hosteler(123,"80k")
ds1=DS(234,"20k")
#In abstract class,object is created then child class must be implemented.
