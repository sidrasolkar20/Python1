'''Aim:Write a Program in python to demonstrate user defined exception. (month no.is input 1-12, above 12 is exception).'''
# Name: Sidra Solkar
# UIN: 231P087
# Roll No: 43
class InvalidMonthError(Exception):
    """Custom exception for invalid month number"""
    pass
def get_month():
    try:
        month = int(input("Enter a month number (1-12): "))
        if month < 1 or month > 12:
            raise InvalidMonthError("Invalid month! Please enter a number between 1 and 12.")
        print(f"Month {month} is valid ✅")
    except InvalidMonthError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter a valid integer.")
get_month()
print("Name: Sidra Solkar \nUIN: 231P087 \nRoll No: 43")
