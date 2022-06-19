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

def greatest():
    a=int(input("Enter number : "))
    b=int(input("Enter number : "))
    if a >=b :
        print(a)
    else:
        print(b)
greatest()

#question2
x,y,z=10 ,20, 30
total=x+y+z
print(total)
kanamba=165

sum=0
for x in str(kanamba):
    sum+=int(x)
    print( sum)
#swap in python
x = 5
y = 10
y,x=x,y
print("x =", x)
print("y =", y)