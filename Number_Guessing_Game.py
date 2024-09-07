from random import randint

lower_num = int(input("enter the number to start point for guess: "))
higher_num = int(input("enter the number to end point for guess: "))

random_number: int = randint(lower_num, higher_num)
print(f'Guess the number in the range from {lower_num} to {higher_num}.')

while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print("Please enter a valid number.")
        continue
    
    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print("you guessed it!")
        break