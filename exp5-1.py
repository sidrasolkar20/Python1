'''Aim:WAP to create a user-defined exception where the program will ask the user to input a number again and again until the user enters the correct stored number.'''
# Name: Sidra Solkar
# UIN: 231P087   Roll No: 43
class WrongNumberError(Exception):
    """Custom exception for incorrect number input"""
    pass
correct_number = 29  
while True:
    try:
        user_input = int(input("Enter the correct number: "))
        if user_input != correct_number:
            raise WrongNumberError("Incorrect number! Try again.")
        print("Congratulations! You entered the correct number.")
        break  
    except WrongNumberError as e:
        print(e)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
print("Name: Sidra Solkar \nUIN: 231P087\nRoll No: 43")
