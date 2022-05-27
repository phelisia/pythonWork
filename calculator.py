
def add(a,b):
    answers=a+b
    return answers
def subtract(a,b):
    answers=a-b
    return answers
def mutiply(a,b):
    answers=a*b
    return answers
def divide(a,b):
    answers=a/b
    return answers
def exponent(a,b):
    answers=a**b
    return answers
def int_divide(a,b):
    answers=a//b
    return answers    
def modulus(a,b):
    answers=a%b
    return answers     
def square(a):
    answers=a*a
    return answers  
def cube(a):
    answers=a**3
    return answers                      

def factorial(n):
    factor=1
    for i in range(1,n+1):
        factor*=i
    return(factor)
