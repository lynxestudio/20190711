class Person:

    def __init__(self,name,lastname,birthdate):
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate
        
    def Talk(self):
        print (" My name is ",self.name," ",self.lastname)
        print (" I was born in ",self.birthdate)

class Employee(Person):

    def Identify(self,employeeid,ssn):
        self.employeeid = employeeid
        self.ssn = ssn
        print(" My employee number is: ",self.employeeid)
        print(" My social security number is: ",self.ssn)

    def ShowEarnings(self,hourlyRate,hoursWorked):
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked
        self.salary = hourlyRate * hoursWorked
        print(" My salary is: ",self.salary)

print("\n")
Martin = Person("Martin","Marquez","29/11/1977")
Martin.Talk()
print("\n")
John = Employee("John","Scoto","29/11/1989")
John.Talk()
John.Identify("34567","5678-9876-4389")
John.ShowEarnings(5.12,16)
print("\n")
