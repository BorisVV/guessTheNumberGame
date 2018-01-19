''' Computer should think of a random number within a certain range,
    and challenge the user to guess the number.
    Provide feedback and hints for the user: such as "too high" or "to low"
'''

print("Hello, and welcome!")
print("Guess a number between 1 an 20, \nif you guess it right you win \
    \nor else you loose, hints will be given; to high or to low")

import random
computer_number = random.randint(1, 20)

def user_number():
    ''' This is to check that the number is an integer. '''
    while True:
        try:
            user_guess = int(input("Enter your number: "))
            # if the number entered is not between 1 and 20 continue the while loop.
            if user_guess < 1 or user_guess > 20:
                print("Enter a number between 1 and 20: ")
                continue
            else:
                break
        # If the user enters something else, the program will not stop and will print a warning.
        except:
            print("Enter a number like 1 or above")
    return user_guess
    # The return is used because we need the number that the user enters.

while True:
    user_input = user_number()
    print(user_input)
    if user_input > computer_number:
        print("Your guess is too high!")
        continue
    elif user_input < computer_number:
        print("Your guess is too low!")
        continue
    else:
        print("You won!!!! \nYou matched the computer number")
        break
