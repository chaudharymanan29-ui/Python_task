import random
print("Welcome to Guess a number game!")
computer = random.randint(1, 10)
you = int(input("Enter number to guess: "))
print(f"computer number  {computer}  \n  You guess  {you}")
if(you>10 or you <=0):
    print("Invalid Input!")
else:
    if(computer==you):
        print("You guess it right buddy!")
    else:
        print("Better luck next time!")

   