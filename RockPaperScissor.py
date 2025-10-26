import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
print("Welcome to Rock Paper Scissor Game..!!!")

game_images=[rock,paper,scissor]

user_choice = int(input("What do you want to choose.?? Type 0 for Rock, 1 for Paper or 2 for scissor. "))
if user_choice >= 0 and user_choice <= 2:
    print("\nYou chose: ")
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win..!!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose..!!")
elif user_choice > computer_choice:
    print("You win..!!")
elif user_choice < computer_choice:
    print("You lose..!!")
elif user_choice == computer_choice:
    print("It's a draw..!!")
else:
    print("Type valid input..!!")