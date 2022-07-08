# var="james bond"
# print(var[2::-1])
# sample={"jodi","jik","deg"}
# sample.add("vick")
# print(sample)
# varr="james" *4 *6
# print(varr)
# for i in range (10,15,1):
#     print(i,end=",")
# def t(n,m=6):
#     res=n*m
#     print(res)

# t(5,4)   

# x= 36/4*(3+2)*4+2
# print(x)
# sampleString ="google.com"

# for x in sample:
#     print(f"g{len(x)}")


# #copying in python
# my_foods = ['pizza', 'falafel', 'carrot cake']
# v =friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# def greatest():
#     a=int(input("Enter number : "))
#     b=int(input("Enter number : "))
#     if a >=b :
#         print(a)
#     else:
#         print(b)
# greatest()

# #question2
# x,y,z=10 ,20, 30
# total=x+y+z
# print(total)
# kanamba=165

# sum=0
# for x in str(kanamba):
#     sum+=int(x)
#     print( sum)
# #swap in python
# x = 5
# y = 10
# y,x=x,y
# print("x =", x)
# print("y =", y)
# import math
# from operator import ne
# #giving a string value
# sent = 'children are playing'
#  #getting the length of the string
# sent_len = len(sent)
#  #get the middle part of the string
# half_string = math.ceil(sent_len/2)
#  #creating 
# part_a = ''
# part_b = ''
 
# part_a = sent[:half_string]
# print(part_a)
# new_part_a = part_a.upper()
 
# part_b = sent[half_string:sent_len]

 
# changed_string = new_part_a+part_b
 
# print(changed_string)
# #quiz2
# previous_num = 0

# # loop from 1 to 10
# for x in range(1, 11):
#     summ=x+previous_num
    
#     print(f"Current Number, {x} Previous Number { previous_num},  Sum: , {summ}")
#     # modify previous number
#     # set it to the current number
#     previous_num=x
# # quiz3

# accept_input=input("Enter a string")
# length=len(accept_input)
# for i in range(0, length - 1, 2):
#     print("index[", i, "]", accept_input[i])
# # you can use slicing
# x=list(accept_input)
# for i in  x[0::2]:
#      print(i)
   
# m=x[0::2]
# print(m)
# #Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# firstnum=numbers_x[0]
# lastnum=numbers_x[-1]
# if firstnum==lastnum:
#     print("True")
# else:
#     print("false")    
# b=[1,2,3,4,56,]

# for a in b:
#     if a==56:
#         print("true")
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# newlist=[]
# def new():
#     for x in list1:
#         if x%2!=0:
#             newlist.append(x)
#             print(newlist)
#     for y in list2:
#         if y%2==0:
#             newlist.append(y)   
#             print(newlist)     
# new()     
# #Write a Program to extract each digit from an integer in the reverse order.
# def palindrome(number):
#     print("original number", number)
#     original_num = number
    
#     # reverse the given number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10

#     # check numbers
#     if original_num == reverse_num:
#         print("Given number palindrome")
#     else:
#         print("Given number is not palindrome")

# palindrome(121)
# palindrome(125)  
#multiplication table2



for x in range(1,11):
    for m in range(1,11):
        print(f"{x}*{m}={x*m}")  
    

# 3: Convert Decimal number to octal using print() output formatting
num=8
print('%o' % num)  
# getting two decimal   
numm = 458.541315
print('%2.f'%numm)      
str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)
howsplitworks="God loves me"
print(howsplitworks.split())
#writing in afile
with open("test.txt", "r") as f:
#    f.write("line1\n")
#    f.write("line2\n\n")
#    f.write("line3\n")
#    f.write("line4\n")
#    f.write("line5\n")
 line = f.readlines()
 print(line[2])

 decimal=23456.789
 print('%2.f'%decimal)
 asdf="Rodger Torach"
 fg=asdf
#  joining
internship="WE HAVE ALL SECURED AN INTERNSHIP IN JESU NAME"
ukweli=internship.split()
print(ukweli)
wasichana="wakenya in warembo sana "
print(wasichana,sep='**')