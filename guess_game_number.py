c = 0
print("Welcome to the guess number game\nGuess the number from 1 to 20")
import random
a = random.randint(1,20)
while True :
    guess = int(input("Enter the number : "))
    if guess ==  a:
         print("You win the game the number is ",a)
         break
    elif guess > a:
         print("Your guess number is high than the right number")

    else:
         print("Your guess number is low than the right number")
    if c == 4 :
         print("you are loser")
         break
    c += 1
