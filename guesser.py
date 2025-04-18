import random
import sys


def main():

    start = input("Type in your guess start range here: ")
    trials = input("Type in your no of trials here: ")
    amount = input("Type in amnount you want to stake here: ")
    odds = input(
        "Type in your guess odds here - odds must be greater than 6: ")

    if not start.isdigit() or not odds.isdigit() or not trials.isdigit() or not amount.isdigit():
        print("invalid input")
        sys.exit()

    start = int(start)
    odds = int(odds)
    amount = int(amount)
    trials = int(trials)

    if odds < 6:
        print("Odds can't be less than 6")
        sys.exit()

    guesses = 0
    random_no = random.randint(start, start + odds)
    while True:
        if trials < 1:
            print(
                f"Sorry you have completed you trials and you lost £{amount:,.2f}!")
            sys.exit()

        guess = input(
            f"Input your guess here. Tip guess between {start} to {start + odds}: ")

        if not guess.isdigit():
            print("Guesses must be numbers only!")
            continue
        else:
            guess = int(guess)
            guesses += 1
            if guess < start or guess > start + odds:
                print(f"Your guess must be between {start} to {start + odds}")
                continue

            if guess != random_no:
                trials -= 1
                print(
                    f"Incorrect guess you have {trials} {"trials" if trials > 1 else "trial"} remaining, please try again")
                continue
            else:
                earnings = (amount*odds)/trials + amount
                print(
                    f"Correct, you have won £{earnings:,.2f} in {guesses} {"guesses" if guesses > 1 else "guess"}")
                sys.exit()


if __name__ == "__main__":
    main()
