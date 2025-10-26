print("Welcome to Treasure Game..!!")
print("Your mission is to find the treasure..!!")

choice1 = input('You\'re at a crossroad. Where do you want to go? "Left" or "Right" \n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for boat or "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input('You\'ve reached island. There is a house with three doors of colours "Red" "Yellow" "Blue". \n').lower()
        if choice3 == "red":
            print("You entered a room full of fire. Game Over. ")
        elif choice3 == "yellow":
            print("Hurray..!!! You found the Treasure. ")
        elif choice3 == "blue":
            print("You entered a room of beasts. Game Over. ")
        else:
            print("You chose a  door that doesn't exist. Game Over. ")
    else:
        print("You're attacked by an Alligator. Game Over. ")
else:
    print("You fell in a hole. Game over.")        
