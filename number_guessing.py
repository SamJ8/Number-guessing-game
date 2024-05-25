import random
from colorama import Fore, init
init(autoreset=True)

random_number = random.randint(1, 22)

number_of_guess = 0


while True:
    try:
        users_guess = int(input(Fore.YELLOW + "\nEnter a number between 1 and 21: "))
    except ValueError:
        print(Fore.LIGHTRED_EX + "Number must be between 1 and 21")
        continue
    
    while users_guess not in range(1,22):
        print(Fore.LIGHTRED_EX + "Number must be between 1 and 21")
        try:
            users_guess = int(input(Fore.YELLOW + "\nEnter a number between 1 and 21: "))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Number must be between 1 and 21")
            continue

    if users_guess == random_number:
        print(Fore.GREEN + "Congratulations, you guessed right!")
        break
    else:
        if users_guess < random_number:
            print(Fore.LIGHTRED_EX + "You guessed too low!")
            
        elif users_guess > random_number:
            print(Fore.LIGHTRED_EX + "You guessed too high!")
        number_of_guess +=1
    
    if number_of_guess == 3:
        print(f"\nThe number was: {random_number}")
        print(Fore.RED + "\nGame over!")
        break

#! end of program