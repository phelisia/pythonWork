def hello ():
    print('Hello AnitaB')
  
#once afunction is defined it cn be imported and reused in another file or class
# a function can accept one or more arguments
def hello(name,age):
    year=2022-age
    print(f"Welcome to AkiraChix")
    return f"Hello {name}, you were born int\t{year}"
    #synatarules
    #Afunction name cannot start with a number
    #Afunction name cannot contain spaces
    #CONVECTIONAL RULES
    #A function name should be in lowercase
    #if a function name has more than one word you should combine them using underscore
    #a function name should you reflect what it does

    #return keyword
   #A function can have an optional return keyword which ends the function and optionally returns a value
#
def my_contry(country="Uganda",student="phelisia"):
    return f"hello{student} you are from{country}"
def greet_mutiple(*names):
    for name in names:
        print(f"hello{name}")

def sum(*namabari):
    total=0
    for m in namabari:
        total+=m
        return total
def muti(*mult):
    t=1
    for m in mult:
        t*=m
        return t
def greet_mu(**kwargs):
    keys=kwargs.keys()
    if "country" in keys:
        print(f"hello {kwargs['name']} you are from {kwargs['country']}")
    elif "age" in kwargs:
        print (print(f"hello {kwargs['name']} you were born in {kwargs['year']}"))
    elif not kwargs:
        f"Hello anonymous"      
def sum_and_greet (*args,**kwargs):
    sum=0
    for num in args:
        sum+=num
    keys=kwargs.keys()
    if 'name'  in keys:
        print(f"hello{kwargs['name']} the answer is{sum}")
    elif  'country' in keys:
        print(f"hello{kwargs['name']} from{kwargs['country']} the answer is{sum}")
    elif not kwargs:
        print(f"hello anonymous the answer is{sum}")           



