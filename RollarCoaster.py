print('Welcome to Roaller Coaster..!!')

height=float(input('What is your height? '))

bill=0
if height >= 120:
    age=float(input('What is your age? '))
    print("You can ride :) ")

    if age <= 12:
        bill = 5
        print("Child ticket is $5")
    elif age <=18:
        bill = 7
        print("Youth ticket is $7")
    else:
        print("Adult ticket is $12")

    photo = input("Do you want photo? Type y for yes and n for no. ")

    if photo == "y":
        bill +=3

    print(f"Your bill is ${bill}")    
else:
    print("You can't ride sweety ")        
