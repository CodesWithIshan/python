
import random 

num = random.randint(1, 100)
attempts = 0

while True:
    try:
        a = int(input("Guess a number between 1-100: "))
        attempts += 1

        if a == num:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
        elif a > num:
            print("Too High! Try a smaller number.")
        else:
            print("Too Low! Try a bigger number.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
