import random
jackpotNumber = random.randint(1, 100)
counter = 1;

guessNumber = int(input("Enter the number you guess could be the jackpot"))

while jackpotNumber != guessNumber :
    if guessNumber < jackpotNumber :
        print("Guess Higher Number")
    else :
        print("Guess Lower Number")
    counter+=1;
    guessNumber = int(input("Try Again!..")) 

print("Congratulations!.. you won the jackpot")
print("You took", counter, "attempts")