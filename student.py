
# Python program to demonstrate
# use of a class method and static method.


from re import S


class Student:
    name="Phelisia"
    age=23
    country="Kenya"
    School="AkiraChix"
class Student:  
    school="AkiraChix"  
    def __init__(self,firstname,lastname,age,country,school,initial):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
        self.school=school
        self.initial=initial
    def greeting(self):
            return f"hello{self.firstname} {self.lastname}you are {self.age} and you were born in with short name {self.initial}from {self.country} welcome to{self.school}"

    def fullname(self):
        full= self.firstname + self.lastname
        return full

    def initial(self):
        initiate=self.firstname[0].split() +self.lastname[0].split()
        return initiate  
       
    def year(self,current_year):
        birthdate=current_year-self.age
        return birthdate   
        