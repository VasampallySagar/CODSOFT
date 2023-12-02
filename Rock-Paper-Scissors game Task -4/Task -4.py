import random as t
user_score = 0
com_score = 0
print("1.rock 2.scissor.3.paper")
a = ["rock", "scissor", "paper"]
while True:
    com = t.choice(a)
    c = int(input("Enter the choice (1 for rock, 2 for scissor, 3 for paper): "))
    
    if c not in [1, 2, 3]:
        print("Invalid input! Please enter a number between 1 and 3.")
        continue
    if c == 1:
        user = "rock"
        print("User chose rock")
    elif c == 2:
        user = "scissor"
        print("User chose scissor")
    else:
        user = "paper"
        print("User chose paper")

    if user == com:
        print("It's a tie!")
    elif (user == "rock" and com == "scissor") or (user == "scissor" and com == "paper") or (
            user == "paper" and com == "rock"):
        print("User won the match!")
        user_score=user_score+1
    else:
        print("Computer won the match!")
        com_score=com_score+1
    print("The score of user is:", user_score)
    print("The score of computer is:", com_score)
    again = int(input("To play again, press 1. To exit, press any other number: "))
    if again != 1:
        print("Program stopped")
        break  
