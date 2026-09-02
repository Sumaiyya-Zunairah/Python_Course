secretNum = 7



def numGeuss():    
    guess = int(input("Guess the number: "))

    while guess != secretNum:
        print("Wrong! Try again!")
        guess = int(input("Guess the number: "))

numGeuss()
print("You got it!")
answer = input("Would you like to play again? Type Yes to contine")
if answer == "Yes":
    numGeuss()
else:
    print("Thanks for playing!")
