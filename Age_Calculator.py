print("----- Welcome to Age Calculator! -----")
from  datetime import datetime
try:
    birth_year = int(input("Enter your birth year: "))
    
    if birth_year == 0:
        print("Enter a valid birth year!")
    else:
        current_year = datetime.now().year
        
        if birth_year > current_year:
            print("Enter a correct birth year bro!")
        else:
            age = current_year - birth_year
            print(f"You are {age} years old.")
except ValueError:
    print("Your birth year is a text?! cool.")
