


class Phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

# For you to print objects you must overide using this 
    def __str__(self) -> str:
        return f"brand\t{self.brand} \tprice\t{self.price}" 
    def capture(self,camera):
        return f"{self.brand} is capturing an amazing pgoto in one two {camera}"
        



iphone=Phone(brand="iphone 7+",price="1400")  
Samsung=Phone(brand="samsung s20",price="1400")  
print(Samsung.capture("chaaaaaa"))
# creating files
#w is for  writing a is for appending r is for reading and r"w is for reading and writing 
# f=open("demofile.txt","r")
# f.write("Id=36668928\nName=Phelisia Jeruto\nEmail=phelisiajeruto@gmail.com")
# f.write("Id=36668928\nName=Phelisia Jeruto\nEmail=phelisiajeruto@gmail.com")
# f.write("Id=36668928\nName=Phelisia Jeruto\nEmail=phelisiajeruto@gmail.com")
#when i want to read a file line by line
# for line in f:
#     print(line)
# f.close()   
# since remebering to close a file after opening is hectic we rather use the with keyword as folows
# 
with open("demofile.txt","r") as file:
    # file.write("Id=36668928\nName=Phelisia Jeruto\nEmail=phelisiajeruto@gmail.com")
    # file.write("Id=36668928\nName=Phelisia Jeruto\nEmail=phelisiajeruto@gmail.com")
    # file.write("Id=36668928\nName=Phelisia Jeruto\nEmail=phelisiajeruto@gmail.com")
    print(file.read())
    
#checking wether a file exist
# import os.path
# file_name="demofile.txt"
# if os.path.isfile(file_name):
#     with open("demofile.txt","r") as file:
#      print(file.read()) 
# else:
#      print  (f"{file_name}file doesnot exist")
print("i")
