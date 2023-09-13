import random  

randomNumbers = random.randint(1,100)
Guess = 0

while Guess != randomNumbers:
    Guess = int(input("Guess the number on my mind: "))
    if Guess < randomNumbers:
        print("Guess Higher!")

    elif Guess > randomNumbers:
        print("Guess Lower!")

print(f"Correct :) i was thinking of {randomNumbers}!")
