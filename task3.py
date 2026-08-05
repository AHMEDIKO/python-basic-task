import random
rounds = 0
won = 0
score = 0
again = 'y'
print("Welcome player")
while again == 'y':
    rounds += 1
    secret = random.randint(1, 100)
    is_won = False
    print("I'm thinking of a number between 1 and 100.")
    for attempt in range(1, 7):
        guess = int(input("Enter your guess: "))

        if guess == secret:
            print("Congratulations! You guessed it!")
            rem = 6 - attempt
            pts = 1 + rem
            score += pts
            won += 1
            is_won = True
            break
        elif guess < secret:
            if (secret - guess) > 15:
                print("Too low")
            else:
                print("Higher")
        else:
            if (guess - secret) > 15:
                print("Too high")
            else:
                print("Lower")
    if not is_won:
        print(f"The number was {secret}")
    again = input("Play again? (y/n): ")
print(f"Rounds Played: {rounds}")
print(f"Rounds Won: {won}")
print(f"Final Score: {score}")