x=range(30)
for y in x:
    if y %3==0:
        print(f"{y%3} is divisible by 3")
    elif y%5==0:
        print(f"{y%5} is divisible by 5")
    elif y%7==0:
        print(f"{y%7} is divisible by 7")
    else:
        print(f"{y} is not divisible by 3,5,7,")
        