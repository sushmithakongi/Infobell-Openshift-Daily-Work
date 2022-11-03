'''
class Test:
    pass

class Dog:
    def details(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Dog name is", self.name,"and age",self.age)
p=Dog()
m=Dog()
p.details("Philo",5)
m.details("Mikey",6)
p.display()
m.display()

class Dog:
    species='mammal'
    def details(self):
        self.name=input("Enter dog name: ")
        self.age=input("Enter dog age: ")
    def display(self):
        print("Dog name is", self.name,"and age",self.age,"Species: ",self.species)
p=Dog()
m=Dog()
p.details()
m.details()
p.display()
m.display()

class DBDA:
    def info(self,rollno,name,groupno,groupname):
        self.rollno=rollno
        self.name=name
        self.groupno=groupno
        self.groupname=groupname
    def display(self):
        print("Student's with their information is Roll no.{} Name {} Group no.{} Group name {}".format(self.rollno,self.name,self.groupno,self.groupname))
s1=DBDA()
s1.info(58,'Vishal Khetmalis',6,'Cluster champs')
s1.display()

class Car:
    def __init__(self,speed,unit):
        self.speed=speed
        self.unit=unit
        self.unit=unit
    def display(self):
        print("Car with max speed of:",self.speed,self.unit)
c1=Car(65,'km/s')
c1.display()
c2=Car(75,'km/s')
c2.display()

class Vehicle:
    wheel='4W'
    count=0
    def __init__(self,wheel):
        self.wheel=wheel
        
class Car:
    def __init__(self,model,price,engine):
        self.model=model
        self.price=price
        self.engine=engine
        Vehicle.count+=1
    def display(self):
        print("Details of Car {} {} Rs.{} {}".format(self.model,Vehicle.wheel,self.price,self.engine))
c=Car('Maruti 800',325000,'Front engine Petrol')
print("object count {}".format(Vehicle.count))
c.display()
c2=Car('Honda Verna',825000,'Front engine Diesel')
print("object count {}".format(Vehicle.count))
c2.display()
'''
