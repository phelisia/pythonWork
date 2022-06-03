from math import pi
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self) :
        area_of_a_circle= pi*self.radius**2
        return f"the area  of the circle is\t{area_of_a_circle}"
    def circumfrence(self):
        circum=2*pi*self.radius
        return  f"the circumfrence  of the circle is\t{circum}"
      

ar=Circle(radius=9)
print(ar.radius)
print(ar.area())  
print(ar.circumfrence()) 

#class square
class Square:
    def __init__(self,side):
        self.side=side
    def area_of_a_square(self):
        area=self.side**2
        return f"The area of a square is\t{area}" 
    def perimeter(self):
        peri=4*self.side
        return  f"the perimeter is\t{peri}"
square1=Square(side=4)
print(square1.side)   
print(square1.area_of_a_square())    
print(square1.perimeter())

#class rectangle
class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area_of_a_rectangle (self):
        area=self.length*self.width
        return f"area of a rectangle is\t{area}"
    def preimeter(self):
        peri=2*self.length+self.width*2
        return f"The perimeter of a rectangle is \t{peri}"  
rectangle1=Rectangle(width=5,length=7)
print(rectangle1.length)  
print(rectangle1.width)       
print(rectangle1.area_of_a_rectangle())
print(rectangle1.preimeter())

#class Sphere
class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def surface_area(self):
        surface_area=4*pi*self.radius*2  
        return f"the surface area  of the sphere is\t{surface_area}" 
    def volume(self):
        vol=1.33333333333*pi*self.radius**3
        return f"The volume of the sphere is\t{vol}"
sphere_one=Sphere(radius=10)
print(sphere_one.radius) 
print(sphere_one.surface_area())      
print(sphere_one.volume())   


    


        
 

